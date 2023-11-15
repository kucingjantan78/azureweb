from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/m')
def members():
    return render_template('members.html')

@app.route('/a')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)







