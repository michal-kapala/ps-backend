from flask import Flask, jsonify, request
import jwt
import datetime
import mongoengine as db
from passwords import db_pass, jwt_key
from models import Post, Like, User

app = Flask(__name__)

db_name = "postscriptum_db"
db_uri = f"mongodb+srv://mongoUser1:{db_pass}@ps-backend-cluster.8mjxg.mongodb.net/{db_name}?retryWrites=true&w=majority"
db.connect(host=db_uri)


@app.route("/auth/login", methods=['POST'])
def login():
    req = request.get_json()

    # db access
    user = User.objects(email=req['email'], password=req['password']).first()
    if user != None:
        jwt_payload = {
            "exp": datetime.datetime.now() + datetime.timedelta(minutes=10)
        }
        token = jwt.encode(payload=jwt_payload, key=jwt_key)
        return jsonify({
            "token": token,
            "user_id": user.user_id,
        }), 200
    else:
        return "", 401

@app.route("/auth/logout", methods=['POST'])
def logout():
    req = request.get_json()
    # revoke jwt validity here
    return "", 204

@app.route("/posts", methods=['GET'])
def get_posts():
    user_param = request.args.get('user_id')
    posts = Post.objects()
    result = []
    for p in posts:
        result.append(p.to_dict())

    # append 'liked' field
    likeSet = Like.objects(user_id=user_param)
    likes = []

    for l in likeSet:
        likes.append(l.to_dict())

    to_update = []

    for l in likes:
        to_update.append(l['post_id'])

    for dict in result:
        if dict['id'] in to_update:
            dict['liked'] = True

    # weird but it returns 1-element list instead of string
    for p in result:
        p['datetime'] = p['datetime'][0]

    return jsonify(result), 200
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

