from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == "__main__":
    # o host deve ser '0.0.0.0' para que o app seja acessível fora do container
    app.run(host='0.0.0.0', port=5000)