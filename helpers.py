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

""" # if not isinstance(ride_id, int):
            # return jsonify({"error": "ride_id should be of type integer"})

        if len(User.rides_list) < 1:
            return jsonify({"message": "No ride offers currently available"})
        else:
            if len(User.rides_request) < 1:
                count = 0
                for dic in User.rides_list:
                    count += 1
                    for key in dic:
                        for ride in dic[key]:
                            if int(ride['ride_id']) == int(ride_id):
                                User.rides_request.append(
                                    {ride_id: [{"username": creating_user.username}]})
                                return jsonify({"Ride requests": User.rides_request})
                            else:
                                if len(User.rides_list) == count:
                                    return jsonify({"No ride offer with ride_id {}".format(ride_id)})
                                else:
                                    continue

            else:
                count = 0
                for dic in User.rides_list:
                    count += 1
                    for key in dic:
                        for ride in dic[key]:
                            if int(ride['ride_id']) == int(ride_id):

                                # User.rides_request.append({ride_id: [{"username": creating_user.username}]})
                                # rides_requests = [{ride_id: [{"username": ""}, {"username": ""}]}, {ride_id:
                                #  [{"username": ""}, {"username": ""}]}]
                                count_request = 0
                                for dic_request in User.rides_request:
                                    count_request += 1
                                    for key_request in dic_request:
                                        if int(key_request) == int(ride_id):
                                            dic_request[key_request].append({"username": creating_user.username})
                                            return jsonify({"Ride requests": User.rides_request})
                                        else:
                                            if len(User.rides_request) == count_request:
                                                User.rides_request.append(
                                                    {ride_id: [{"username": creating_user.username}]})
                                                return jsonify({"Ride requests": User.rides_request})
                                            else:
                                                continue

                            else:
                                if len(User.rides_list) == count:
                                    return jsonify({"No ride offer with ride_id {}".format(ride_id)})
                                else:
                                    continue

"""