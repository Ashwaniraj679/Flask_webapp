from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'

@app.route('/')
def home_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug= True)