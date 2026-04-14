"""
Keep-Alive Server for Render.com
Prevents the bot from spinning down due to inactivity on the free tier.
"""

from flask import Flask
import logging
from threading import Thread

# Initialize logger
logger = logging.getLogger(__name__)

# Create Flask app
app = Flask(__name__)


@app.route('/')
def home():
    """Simple health check endpoint."""
    return {"status": "alive", "message": "Bot is running!"}, 200


@app.route('/health')
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}, 200


def run_server():
    """Run the Flask server on 0.0.0.0:8080."""
    try:
        logger.info("Starting keep-alive server on 0.0.0.0:8080")
        app.run(host='0.0.0.0', port=8080, debug=False, use_reloader=False)
    except Exception as e:
        logger.error(f"Error running keep-alive server: {e}")


def start_keep_alive():
    """
    Start the keep-alive server in a separate thread.
    This prevents the main bot thread from being blocked.
    """
    server_thread = Thread(target=run_server, daemon=True)
    server_thread.start()
    logger.info("Keep-alive server thread started (daemon mode)")
    return server_thread
