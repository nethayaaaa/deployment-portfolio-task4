from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    app_environment = os.getenv("APP_ENV", "Development")
    student_name = os.getenv("STUDENT_NAME", "Student")

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Docker Deployment Status</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f6f8;
                text-align: center;
                padding-top: 80px;
            }}

            .container {{
                width: 500px;
                margin: auto;
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            }}

            .success {{
                color: green;
                font-weight: bold;
            }}
        </style>
    </head>

    <body>
        <div class="container">
            <h1>Docker Deployment Status</h1>

            <p class="success">
                Container is running successfully
            </p>

            <p><strong>Student:</strong> {student_name}</p>

            <p><strong>Environment:</strong> {app_environment}</p>

            <p><strong>Task:</strong> SWE40006 Deployment Portfolio Task 4.3</p>

            <p><strong>Server Time:</strong> {datetime.now()}</p>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)