# Flask Chat Application with Spam & Offensive Content Filtering

![Chat Application Demo](screenshot.png)  
*Example screenshot of the chat interface*

---

## Overview
This Flask-based web application provides a real-time chat interface with:
- Offensive language filtering
- Advanced spam detection
- User-friendly warnings
- Message history

---

## Features

### Core Functionality
- ✅ Real-time chat interface
- ✅ User authentication (optional)
- ✅ Message timestamping
- ✅ Responsive design

### Security & Moderation
- 🔒 Offensive word filtering
- 🚫 Spam detection (URLs, scams, phishing, etc.)
- ⚠️ User warnings for policy violations
- ⏱️ Rate limiting to prevent flooding

---

## Installation

### Prerequisites
- Python 3.8+
- `pip` package manager

### Setup Steps
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/flask-chat-app.git
   cd flask-chat-app

2. **Create environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```
3. ***Install dependencies***

    ```
    pip install -r requirements.txt
    ```