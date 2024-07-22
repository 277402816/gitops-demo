from flask import Flask
app = Flask(__name__)

@app.route('/demo2')
def hello_world():
    return 'Hello, World22!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)