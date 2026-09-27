from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Deployment Portfolio Task 4.2</h1>
    <p>Python Flask application is running successfully inside Docker.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)