import os
import logging
from binance.client import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class BasicBot:
    def __init__(self, api_key=None, api_secret=None, testnet=True):
        # Grab keys from args or environment
        self.api_key = api_key or os.getenv("BINANCE_API_KEY")
        self.api_secret = api_secret or os.getenv("BINANCE_API_SECRET")

        if not self.api_key or not self.api_secret:
            raise ValueError("Missing API keys. Add them to your .env file or pass explicitly.")

        # Initialize Binance client
        self.client = Client(self.api_key, self.api_secret, testnet=testnet)

        # Point to the Futures Testnet endpoint
        if testnet:
            self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        # Setup logging
        logging.basicConfig(
            filename="bot.log",
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s"
        )
        logging.info("BasicBot initialized (testnet=%s)", testnet)

    def get_account_info(self):
        """Fetch account info to check connection."""
        try:
            info = self.client.futures_account()
            logging.info("Fetched account info")
            return info
        except Exception as e:
            logging.error(f"Error fetching account info: {e}")
            return {"error": str(e)}
