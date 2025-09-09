# Binance Futures Testnet Bot (Simplified)

Structure:

[project_root]/
├── src/
│   ├── market_orders.py
│   ├── limit_orders.py
│   ├── client.py
│   └── advanced/
│       ├── oco.py
│       └── twap.py
├── bot.py
├── bot.log
├── report.pdf
└── README.md

Setup:
1. Create a Binance Futures Testnet API key at https://testnet.binancefuture.com
2. Set BINANCE_API_KEY and BINANCE_API_SECRET env vars or pass them to scripts.
3. Install dependencies:
   pip install requirements.txt

Usage:
- Examples are in src/market_orders.py and src/limit_orders.py.
- Educational/demo code. Use only on testnet.
