from flask import Flask

app = Flask(__name__)  # Dunder is short for double underscore.


@app.route('/')  # a route is something that maps a URL path to a function.
def home():
    return """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    Hello Flask World!
</body>
</html>
    
    """


if __name__ == '__main__':
    app.run(debug=False)  # runs on a local dev server with debug set on if True.
    # detects if changes have been made and restarts the app automatically.
