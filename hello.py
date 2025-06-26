from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<html><h2>Hello World!!</h2></html>"


if __name__ == '__main__':
    app.run(debug=True)