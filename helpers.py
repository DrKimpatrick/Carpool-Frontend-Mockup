from flask import request, jsonify
from api_classes import User


def get_users(user_list, name, email, username, phone_number, bio, gender, password):

    for user in user_list:
        # username already exists
        if user['username'] == request.json['username']:
            return jsonify(
                {"message": "Username already taken, try another"}
            )

        # username does not exist
    else:
        creating_user = User(
            name,
            email,
            username,
            phone_number,
            bio, gender,
            password
        )
        creating_user.signup()
        return jsonify({"Users": creating_user.users_list})

"""
if len(User.users_list) < 1:
    return jsonify(
        {"message": "Your username or password is incorrect"}
    )
else:
    count = 0
    for user in User.users_list:
        count += 1

        if user['username'] != username:
            if len(User.users_list) != count:
                continue
            else:
                return jsonify(
                    {"message": "Your username or password is incorrect"}
                )
        else:
            if user['password'] == password:
                return jsonify({"message": "You are logged in"})
            else:
                return jsonify(
                    {"message": "Your username or password is incorrect"}
                )

"""

"""count = 0
    if len(User.rides_list) < 1:
        return jsonify(
            {"message": "It seems no ride offers available, try again later"}
        )
    else:
        for dic in User.rides_list:
            count += 1
            for key in dic:
                for ride in dic[key]:
                    if int(ride['ride_id']) == int(ride_id):
                        return jsonify(
                            {"Ride": ride}
                        )
                    else:
                        if len(User.rides_list) == count:
                            return jsonify(
                                {"message":
                                 "The ride offer with ride_id {} does not exist".format(ride_id)}
                            )
                        else:
                            continue


# rides_list = [{"username_1": [{"origin": "", "destination": ""}]},
                        # {"username_1": [{"origin": "", "destination
    # ": ""}]}]"""