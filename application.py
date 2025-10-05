from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from Elastic Beanstalk!"

# For local run
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

# Elastic Beanstalk expects a callable named 'application' for WSGI
application = app
