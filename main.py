from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/login")
def root():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True, port=5050)