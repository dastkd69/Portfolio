from flask import Flask, render_template, redirect
app = Flask(__name__, template_folder="templates")


globals = {
            'NESRemu' : 'https://github.com/dastkd69/NESRemu',
            'NESRemu' : 'https://github.com/dastkd69/NESRemu',
            'NESRemu' : 'https://github.com/dastkd69/NESRemu'
}


@app.route("/", methods=["GET"])
def showHome():
    return render_template("index.html")

@app.route("/achievements", methods=["GET"])
def showAchievements():
    return render_template("achievements.html")

@app.route("/blog", methods=["GET"])
def showBlog():
    return redirect('https://zenxt.data.blog/')

@app.route("/github", methods=["GET"])
def showGithub():
    return redirect('https://github.com/dastkd69')

# @app.context_processor
# def globals():
#     return globals    



if __name__ == "__main__":
    app.run(debug=True)