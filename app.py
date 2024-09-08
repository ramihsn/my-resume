from flask import Flask
import views

app = Flask(__name__)
app.register_blueprint(views.root, url_prefix='/')


if __name__ == "__main__":
    app.run('localhost', debug=True)
