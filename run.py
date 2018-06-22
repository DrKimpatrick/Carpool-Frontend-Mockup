from flask import Flask, request, jsonify
from api_classes import User

app = Flask(__name__)


@app.route('/api/v1/users/signup', methods=['POST'])
def create_user():

    name = request.json["name"]
    email = request.json['email']
    username = request.json['username']
    phone_number = request.json['phone_number']
    bio = request.json['bio']
    gender = request.json['gender']
    password = request.json['password']
    # check if username already exists
    # users_list = [{"name":"", "email":"", "username":"", "phone_number":"", "bio":"", "gender":"", "password":""}]

    global creating_user  # making it available every where

    if len(User.users_list) < 1:

        creating_user = User(name, email, username, phone_number, bio, gender, password)
        creating_user.signup()
        return jsonify({"Users": creating_user.users_list})
    else:
        count = 0
        for dic in User.users_list:
            count += 1
            # username already exists
            if dic['username'] == request.json['username']:
                return jsonify({"message": "Username already taken, try another"})

            # username does not exist
            else:

                if len(User.users_list) == count:
                    creating_user = User(name, email, username, phone_number, bio, gender, password)
                    creating_user.signup()
                    return jsonify({"Users": creating_user.users_list})
                else:
                    continue


@app.route('/api/v1/users/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    # kim = [{}, {}]
    if len(User.users_list) < 1:
        return jsonify({"message": "Your username or password is incorrect"})
    else:
        count = 0
        for user in User.users_list:
            count += 1

            if user['username'] != username:
                if len(User.users_list) != count:
                    continue
                else:
                    return jsonify({"message": "Your username or password is incorrect"})
            else:
                if user['password'] == password:
                    return jsonify({"message": "You are logged in"})
                else:
                    return jsonify({"message": "Your username or password is incorrect"})


@app.route('/api/v1/users', methods=['GET'])
def list_of_users():
    return jsonify({'users': User.users_list})


if __name__ == '__main__':
    app.run(debug=True)
























































