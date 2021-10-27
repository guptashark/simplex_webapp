import flask
from flask import Blueprint, render_template

simplex_app = Blueprint("simplex_app", __name__, template_folder='templates')

@simplex_app.route("/", methods=["GET"])
def hello():
  return render_template('simplex/simplex.html')

if __name__ == "__main__":
  app = flask.Flask(__name__)
  app.register_blueprint(simplex_app, url_prefix="/simplex")
  app.run(host="localhost", port=8080, debug=True)
