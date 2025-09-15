# My N8N Workflows Collection

Welcome to my collection of N8N workflows! This repository contains various automation workflows created and exported from N8N, covering different use cases and integrations.

## About N8N

N8N is an open-source workflow automation tool that allows you to connect different services and automate tasks through a visual interface. Each workflow in this repository is provided as a JSON file that can be imported directly into your N8N instance.

## Workflows

### Mail Labeling
**File:** `Mail Labeling.json`

This workflow automatically categorizes and labels incoming Gmail messages using AI-powered text classification. It monitors your Gmail inbox every minute and uses the Groq Chat Model (Llama-3.3-70b) to intelligently classify emails into four categories:

- **Sponsorship**: Emails about sponsored content, brand deals, promotions, and partnership opportunities
- **Collaboration**: Messages on teamwork, joint projects, and partnership invitations  
- **Business Inquiries**: Professional requests, client inquiries, and formal business proposals
- **Other**: All other emails that don't fit the above categories

Once classified, the workflow automatically applies the corresponding Gmail labels to organize your inbox efficiently. This helps maintain a clean, organized email system without manual intervention.

