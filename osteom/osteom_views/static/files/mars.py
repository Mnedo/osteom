from flask import Flask
from flask import url_for
from flask import request

app = Flask(__name__)


@app.route('/carousel', methods=['POST', 'GET'])
def countdown():
    if request.method == 'GET':
        text = f"""
        <!DOCTYPE html>
                <head>
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <link rel="icon" href="{url_for('static', filename='img/mars.png')}" type="image/x-icon">
                    <title>Пейзажи Марса</title>
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
                    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
                    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
                </head>
                <body>
                    <div class="h1">
                        <h1>Пейзажи Марса</h1>
                    </div>


                </body>
        """
        return text
        #{url_for('static', filename='img/caros3.jpg')}

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
