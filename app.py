from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/response')
def resp():
    username = request.args.get('username')
    method = request.method
    return render_template('response.html',
            username=username,
            method=method)

if __name__ == '__main__':
    app.run(debug=True);
