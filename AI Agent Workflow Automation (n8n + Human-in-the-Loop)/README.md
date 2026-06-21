# AI Agent Workflow Automation — n8n + Human-in-the-Loop

## What this is

An n8n workflow that takes a social media post topic + schedule (via a form),
generates brand-consistent post copy with an LLM, composites a template-based
image card, routes it to a human reviewer by email, and only publishes (to
mock Facebook/Instagram endpoints) once approved.

## Architecture

```
Form Trigger → Generate & Validate Post (Gemini) → Build Image Card URL (Cloudinary)
            → Email Reviewer — Send & Wait (Gmail)
                  ├── Approved → Mock Publish → Facebook  (parallel)
                  │           → Mock Publish → Instagram  (parallel)
                  └── Rejected → Post Rejected — Log & Stop
```

## Setup

1. **Import** `workflow_social_media_automation.json` into n8n (Import from File).
2. **Fill in 4 placeholders:**

   | Node | Placeholder | Where to get it |
   |---|---|---|
   | Generate & Validate Post | `GEMINI_API_KEY` | aistudio.google.com/apikey — free, no credit card |
   | Build Image Card URL | `CLOUD_NAME` | Cloudinary dashboard, top-left |
   | Build Image Card URL | `BACKGROUND_ID` / `LOGO_ID` | public_id of the two images uploaded to Cloudinary's Media Library |
   | Email Reviewer — Send & Wait | `sendTo` address | your own inbox, for testing |

3. **Connect Gmail** on the Email Reviewer node (OAuth, no app password needed).
4. **Activate the workflow**, open the Form Trigger node, copy its URL, and
   open it in a browser — this shows a real form with **Topic** and
   **Scheduled Date/Time** fields.
5. Submit the form, check your inbox, **approve or reject**.

## Must Explain

### 1. Prompt engineering strategy for the 90–150 word constraint

The constraint is enforced in two layers, not just hoped for:

- **System instruction** states the rule as a hard, explicit requirement
  rather than a soft suggestion — LLMs follow constraints stated up front
  far more reliably than ones implied by example.
- **Programmatic validation, not trust.** After each generation, the code
  node counts words itself (`split(/\s+/)`) rather than trusting the model's
  self-report. If the count falls outside 90–150, it retries — up to 3 times.
- **Adaptive retry feedback.** Each retry tells the model exactly which
  direction it missed and by how much ("your previous attempt had 62 words,
  add more content to reach at least 90"), converging much faster than a
  blind retry.
- **Hard failure over silent truncation.** If 3 attempts all miss the range,
  the node throws an error rather than truncating text mid-sentence.
- **Thinking disabled for this task.** `gemini-2.5-flash` uses an internal
  "thinking" pass by default that consumes the same token budget as the
  visible answer, which on this task produced near-empty output. Setting
  `thinkingConfig: { thinkingBudget: 0 }` routes the full token budget to the
  actual post text — a deliberate, debugged choice rather than a default.

### 2. Image compositing pipeline for pixel-perfect placement

Rather than generating an image with an AI model (unpredictable layout every
run), the card is built with **Cloudinary's URL-based transformation API**.
The image URL is a string built from chained, deterministic parameters —
the same parameters produce the same layout on every run, regardless of topic:

- **Background fade:** `e_colorize:60,co_black` darkens the background by
  60% so white overlay text stays readable regardless of the underlying
  image's brightness. This is listed *first* in the transformation chain so
  it only affects the base image, before the logo or text are layered on.
- **Logo placement:** `l_brand_logo,g_north_east,x_20,y_20,w_120` — pinned to
  the top-right corner with a fixed 20px margin and fixed 120px width, on
  every run.
- **Title placement:** `l_text:Arial_30_bold:{title},g_south,y_40,w_550,h_180,c_fit` —
  anchored to the bottom-center, with a 550×180px box reserved above it. This
  box gives Cloudinary enough room to **wrap long titles across up to three
  lines** rather than truncating them — Cloudinary doesn't support shrinking
  font size to fit a container, but it does support multi-line wrapping when
  given adequate height, so reserving that height was the fix for titles
  that don't fit on one line.
- Text is percent-encoded (not converted to underscores) so that spaces in
  the topic render as actual spaces rather than literal underscore
  characters in the final image.

Because the layout is fully parameterized, three different topics produce
three structurally identical cards — only the title text changes.

### 3. Human approval pause and webhook architecture

n8n's Gmail node has a built-in **"Send and Wait for Approval"** operation:

- When the node runs, it sends the review email and **suspends that workflow
  execution**, persisting its state to n8n's database — no polling, no
  separate tracking table.
- `approvalOptions.values.approvalType: "double"` configures **two** buttons
  (Approve / Reject) rather than the default single Approve-only button.
  Each button is a unique, single-use URL n8n embeds in the email, pointing
  back to a webhook tied to that specific paused execution.
- Clicking a button resumes that exact execution and routes it down one of
  two outputs: output 0 (approved) fans out in parallel to both mock
  Facebook and Instagram publish requests; output 1 (rejected) routes to a
  logging node and the run ends without publishing.

This is a genuine suspended execution, not a sleep loop or cron polling a
database — it resumes exactly where it left off, with all upstream data
(topic, generated text, image URL) intact.

## Known issues fixed during development (worth mentioning in the demo)

- Switched from OpenAI to Google Gemini after hitting a billing-required 429
  on a fresh OpenAI key — Gemini's free tier needs no card.
- Disabled Gemini 2.5 Flash's default "thinking" mode, which was silently
  consuming the entire output token budget and returning near-empty text.
- Corrected the Gmail node's approval-button configuration — the default is
  single-button approval; double approval requires explicitly setting
  `approvalType: "double"` under `approvalOptions.values`.
- Discovered the n8n Form Trigger currently outputs submitted data keyed by
  **Field Label**, not the configured **Field Name** — downstream nodes
  reference fields by their exact label string as a workaround.
- Fixed a text-rendering bug where literal spaces in Cloudinary text overlays
  were being converted to underscore characters; switched to pure percent-
  encoding instead.
- Fixed title truncation (silent ellipsis) on longer topics by giving the
  text layer explicit width *and* height, allowing it to wrap across
  multiple lines instead of being cut off.

## Demo video checklist

- [ ] Submit the form with 3 different topics (one at a time)
- [ ] Show each review email side by side, proving the logo position and
      title position are identical across all three — only the title text
      and length differ
- [ ] Approve one, reject another, show both outcomes (mock publish vs. log)
- [ ] Show the n8n execution log confirming the paused → resumed state
