from flask import Flask, render_template

app = Flask(__name__)  # Dunder is short for double underscore.


@app.route('/')  # a route is something that maps a URL path to a function.
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=False)  # runs on a local dev server with debug set on if True.  False by default.
    # detects if changes have been made and restarts the app automatically.
