from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('input.html')


@app.route("/output", methods=['POST'])
def output():
    # inputタグのname属性を指定する
    your_name = request.form['name']
    return render_template('output.html', name=your_name)

if __name__ == "__main__":
    app.run(debug=True)