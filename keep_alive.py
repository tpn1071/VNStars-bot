from flask import Flask
from threading import Thread

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():     # type: ignore
        return "Bot is alive!"
    

    return app

def run_app():
    app = create_app()
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    """Start a background Flask server to keep the bot alive."""
    thread = Thread(target=run_app, daemon=True)
    thread.start()
