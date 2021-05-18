import webbrowser
from flask import Flask, render_template


app = Flask(__name__, template_folder="templates")


@app.route("/", methods=["GET"])
def showHome():
    return render_template("index.html")

@app.route("/achievements", methods=["GET"])
def showAchievements():
    return render_template("achievements.html")

@app.route("/blog", methods=["GET"])
def showBlog():
    return webbrowser.open('https://zenxt.data.blog/', autoraise=True)

@app.route("/github", methods=["GET"])
def showGithub():
    return webbrowser.open('https://github.com/dastkd69', autoraise=True)



if __name__ == "__main__":
    app.run()


    