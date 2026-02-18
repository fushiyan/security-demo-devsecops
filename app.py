import sqlite3
from flask import Flask, request

app = Flask(__name__)

# ❌ Hardcoded secret (for TruffleHog)
API_KEY = "sk_test_1234567890SECRETKEY" #api key exposed

@app.route("/user")
def get_user():
    username = request.args.get("username")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # ❌ SQL Injection vulnerability (for Semgrep)
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    return "User lookup executed"

if __name__ == "__main__":
    app.run(debug=True)
