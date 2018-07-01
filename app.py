from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index() :
    return render_template('home.html')

@app.route('/home')
def home() :
    return render_template('home2.html')

@app.route('/test')
def test() :
    aa = {
        "a":"1",
        "b":"2"
    }
    return jsonify(aa)

if __name__ == '__main__' :
    app.run(debug=True)