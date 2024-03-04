# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn
from firebase_admin import initialize_app
import flask

initialize_app()
app = flask.Flask(__name__)


@app.get("/users")
def get_users():
    return flask.Response(status=200, response=flask.json.dumps([
        {
            "id": 1,
            "name": "Tanaka"
        },
        {
            "id": 2,
            "name": "Higashi"
        },
        {
            "id": 3,
            "name": "Takashima"
        }
    ]))


@app.post("/user")
def create_user():
    return flask.Response(status=201, response="ユーザー`{}`を作成しました。".format(flask.request.json["name"]))


@https_fn.on_request()
def api(req: https_fn.Request) -> https_fn.Response:
    with app.request_context(req.environ):
        return app.full_dispatch_request()
