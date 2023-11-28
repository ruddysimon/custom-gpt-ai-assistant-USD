# Documentation: Integrating Replit and Voiceflow with OpenAI API
## Overview
This documentation provides a detailed guide on integrating Replit and Voiceflow with the OpenAI API. It involves setting up a Python environment in Replit, configuring Voiceflow, and linking the two platforms for seamless operation.

## Prerequisites
Accounts on Replit and Voiceflow.
OpenAI API key.
Knowledge base files (PDF, DOCX, CSV, etc.).
Python files (main.py and functions.py).

## Procedure
## Configuring Replit
Upload Knowledge Base:
- Log into your Replit account.
- In the left sidebar, upload the knowledge base files (PDF, DOCX, CSV, etc.).

Add OpenAI API Key:

- In the lower part of the left sidebar, locate the 'Secrets' section.
- Click on the 'Secret' button.
- Add your OpenAI API key here.

## Setting Up Voiceflow
Access Workspace:

Log into your Voiceflow account.
- Open the desired workspace.

Upload Voiceflow Template:
- In the assistant section on the left side, upload the Voiceflow template from the 'Voiceflow Template' folder.

Linking Replit with Voiceflow
Run Python File:

Ensure the knowledge base and OpenAI API key are uploaded on Replit.
Run the main.py file.
A webpage will pop up displaying "Not Found".
Copy Webpage Link:

Click on the 'New Tab' on the right side to open a new tab in your web browser.
Copy the URL from this tab.
Configure Voiceflow Template:

Return to Voiceflow and open your template.
In the 'Create Thread' section under 'Get', paste the copied link and append /start to it.
In the 'Generate Response' section under 'Post', paste the same link and append /chat to it.
Testing the Integration
Run the Voiceflow Project:
Click the 'Run' button located at the upper right side of Voiceflow.
Start asking questions to the LLM chatbot through the interface.
The responses will be generated based on the integration with the OpenAI API via Replit.
