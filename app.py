from flask import Flask

app = Flask(__name__)

@app.route('/')
def saudar():
    return"Oi!"

@app.route('/dan')
def saudar_dan():
    return"eae Dan!"

if __name__ =="__main__":
    app.run(debug=True)