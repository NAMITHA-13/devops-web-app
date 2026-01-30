from flask import Flask
import os

print("🔥 NEW CODE IS RUNNING 🔥")
print("APP_ENV =", os.getenv("APP_ENV"))

app = Flask(__name__)

@app.route("/")
def home():
    env = os.getenv("APP_ENV")
    return f"Application is running in {env} environment"

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

