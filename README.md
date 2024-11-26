# Basic IMAP Email Viewer

A simple Python application for retrieving and displaying emails using the IMAP protocol.

## Features
- Connects to an email account via IMAP
- Fetches the latest emails
- Displays the sender, subject, and date of each email

## Requirements
- Python 3.x
- Required libraries: `imaplib`, `email`

## Installation

1. Clone the repository:  
   ```bash
   git clone https://github.com/barisatay0/basic-imap-email-viewer.git
   cd basic-imap-email-viewer
   ```

2. Create and activate a virtual environment:  
   On Linux/macOS:  
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   On Windows:  
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install required libraries:  
   ```bash
   pip install -r requirements.txt
   ```

4. Update the email and password in `main.py`.


5. Run the application:  
   ```bash
   python main.py
   ```
