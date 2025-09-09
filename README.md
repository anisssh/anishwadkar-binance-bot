# BasicBot - Binance Futures Testnet Bot

A simple Python bot to interact with Binance Futures Testnet using API keys. This bot fetches account info and can be extended for trading strategies.

---

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [API Keys](#api-keys)
- [Usage](#usage)
- [Logging](#logging)
- [Notes](#notes)

---

## Features

- Connects to Binance Futures Testnet.
- Fetch account information.
- Logs all actions and errors to `bot.log`.
- Easily extensible for placing orders or other strategies.

---

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- Binance account (for API keys)

---

## Setup

1. **Clone the repository** (or download your files):
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```
2. **Install dependencies**

   pip install -r requirements.txt

3. **Create .env file in your project root**

```bash
   BINANCE_API_KEY=your_api_key_here
   BINANCE_API_SECRET=your_api_secret_here
```

4. **Run the bot**

```bash
   python bot.py
```

5. **Logging**

   All actions and errors are logged to bot.log in the project directory.

   Check bot.log for debugging or monitoring bot activity.
