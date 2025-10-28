from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('myForm.html')

@app.route('/submit', methods=['POST'])
def submit():
    uname = request.form['uname']
    age=request.form['age']
    return render_template('greetings.html', name=uname,age=age)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
