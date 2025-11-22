from flask import Flask, render_template  # type: ignore


# * Run: flask --app server.py run
# * Run: python3 -m flask --app server.py run --debug


app = Flask(__name__)
# print(__name__)  # __main__ / server
# print(app)  # <Flask 'server'>


# @app.route("/")
# def hello_world():
#     return '<h1 style="text-align:center; color: blue">Hello, World!</h1>'


@app.route("/")
def hello_world():
    return render_template("index.html")


# by default 'render_template' looks in the 'templates' folder in the same directory for the given file.
# and the '.html' file might be pointing to '.css' and '.js' file,
# but 'render_template' will only allow those files if they are in 'static' folder.


@app.route("/blog")
def blog():
    return "This is my blog section!"


@app.route("/blog/2020/dog")
def blog_dog():
    return "This blog is about my dog, Rocky!"


@app.route(
    "/blog/<username>/<int:age>"
)  # if we don't specify the variable type, it will be taken as string by default.
def user_blog(username, age):
    return render_template("user_blog.html.jinja", name=username, age=age)
