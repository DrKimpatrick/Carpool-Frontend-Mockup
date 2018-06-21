from flask import Flask, request, jsonify
from api_classes import User

app = Flask(__name__)


@app.route('/users/signup', methods=['POST'])
def create_user():
    name = request.json["name"]
    email = request.json['email']
    username = request.json['username']
    phone_number = request.json['phone_number']
    bio = request.json['bio']
    gender = request.json['gender']
    password = request.json['password']
    global creating_user  # making it available every where

    creating_user = User(name, email, username, phone_number, bio, gender, password)
    creating_user.signup()

    # global creating_user

    return jsonify({"Users": creating_user.users_list})


if __name__ == '__main__':
    app.run(debug=True)
























































