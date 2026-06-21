# My N8N Workflows Collection

Welcome to my collection of N8N workflows! This repository contains various automation workflows created and exported from N8N, covering different use cases and integrations.

## About N8N

N8N is an open-source workflow automation tool that allows you to connect different services and automate tasks through a visual interface. Each workflow in this repository is provided as a JSON file that can be imported directly into your N8N instance.

## Workflows & Projects

### Mail Labeling Workflow
- **File**: `Mail Labeling.json`
- **Purpose**: Automated email classification and labeling system

### AI Agent Doc Reader
- **File**: `AI Agent Doc Reader.json`  
- **Purpose**: AI-powered document reading and analysis workflow

### Article Insights Chatbot Project
- **Folder**: `chatbot-with-article-analysis/`
- **Description**: Complete full-stack application for article analysis and insights generation
- **Tech Stack**: FastAPI + React + TypeScript + N8N + Google Gemini AI
- **Features**: 
  - Web article scraping and analysis
  - Real-time chat interface
  - AI-powered summaries and insights
  - Email notifications
  - Google Sheets data logging

### Ecommerce Automation Test Project  
An n8n workflow that automates ecommerce operations by:  
- Fetching product data from DummyJSON API  
- Updating Google Sheets with product details  
- Extracting order info from Gmail using Google Gemini AI  
- Creating and managing tasks in Monday.com  

### AI Agent Workflow Automation (n8n + Human-in-the-Loop)
An automation workflow built in n8n that takes a social media topic and schedule via form input, generates brand-consistent post copy using Google Gemini, composites a template-based image card via Cloudinary, and pauses for a human email review before publishing to mock social endpoints.
- **Features**:
  - **Form Trigger**: Captures user inputs for post topic and scheduled date/time.
  - **Deterministic Compositing**: Dynamically generates a pixel-perfect image card using parameterized URLs.
  - **Human-in-the-Loop (HITL)**: Suspends execution state and fires an email with dedicated Approve/Reject webhooks.
  - **Parallel Publishing**: Fans out to publish to mock Facebook and Instagram endpoints simultaneously upon approval.

## How to Use These Workflows

1. **Download** the JSON file for the workflow you're interested in
2. **Open** your N8N instance (local or cloud)
3. **Import** the workflow by uploading the JSON file
4. **Configure** the required credentials and connections
5. **Activate** the workflow and start automating!

## Getting Started with N8N

If you're new to N8N:
1. Visit [n8n.io](https://n8n.io) to learn more
2. Try the [cloud version](https://app.n8n.cloud) or install locally
3. Check out the [documentation](https://docs.n8n.io)
4. Join the [community](https://community.n8n.io)
