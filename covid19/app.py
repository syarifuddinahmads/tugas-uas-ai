from flask import Flask ,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diagnosa-pribadi')
def diagnosaPribadi():
    return render_template('diagnosa-pribadi.html')

@app.route('/upload-data-diagnosa')
def diagnosaData():
    return render_template('upload-data-diagnosa.html')


if __name__ == '__main__':
    app.run()
