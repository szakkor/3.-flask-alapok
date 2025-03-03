from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

app.static_folder = "static"
app.template_folder = "templates"

@app.route("/")
def index():
    return """
<h1>
    Hello World
</h1><br>

<p>Ez egy sima szöveg</p>
<a href="/oldal1">Tovább ---></a>

"""

@app.route("/oldal1")
def oldal1():
    return render_template("index.html")




@app.route("/input")
def input():
    return render_template("input.html")

@app.route("/leker", methods=["POST"])
def leker():
    name = request.form['names']
    age = request.form["age"]
    print(f"{name}: {age}")
    return redirect(url_for("input"))


if __name__ == "__main__":
    app.run(debug=True, port=5000)