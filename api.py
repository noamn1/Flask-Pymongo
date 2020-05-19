from flask import Flask, json, request
from db.dataLayer import DataLayer

app = Flask(__name__)

dataLayer = DataLayer()


@app.route("/user/<string:user_id>")
def get_user_by_id(user_id):
    user = dataLayer.get_user_by_id(user_id)
    resp = app.response_class(response=json.dumps(user.to_json()),
                              status=200,
                              mimetype="application/json")

    return resp


@app.route("/user")
def get_user():
    username = request.args.get("username")
    user = dataLayer.get_user(username)
    resp = app.response_class(response=json.dumps(user.to_json()),
                              status=200,
                              mimetype="application/json")

    return resp


if __name__ == "__main__":
    app.run()
