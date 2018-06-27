from flask import Flask, request, jsonify
from api_classes import User

app = Flask(__name__)


@app.route('/api/v1/users/signup', methods=['POST'])
def create_user():
    if (not request.json or
            "name" not in request.json or
            "email" not in request.json or
            "username" not in request.json or
            "phone_number" not in request.json or
            "bio" not in request.json or
            "gender" not in request.json or
            "password" not in request.json):

        return jsonify(
            {
                "error": "Bad request (400). The browser (or proxy) sent a "
                         "request that this server could not understand."
            }
        )

    name = request.json["name"]
    email = request.json['email']
    username = request.json['username']
    phone_number = request.json['phone_number']
    bio = request.json['bio']
    gender = request.json['gender']
    password = request.json['password']

    # check if userpip install coverallsname already exists
    # users_list = [{"name":"", "email":"", "username":"",
    # "phone_number":"", "bio":"", "gender":"", "password":""}]

    global creating_user  # making it available every where

    if len(User.users_list) < 1:

        creating_user = User(
            name,
            email,
            username,
            phone_number,
            bio,
            gender,
            password
        )
        creating_user.signup()
        return jsonify(
            {"Users": creating_user.users_list}
        )
    else:
        count = 0
        for dic in User.users_list:
            count += 1
            # username already exists
            if dic['username'] == request.json['username']:
                return jsonify(
                    {"message": "Username already taken, try another"}
                )

            # username does not exist
            else:

                if len(User.users_list) == count:
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
                else:
                    continue


@app.route('/api/v1/users/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    # kim = [{}, {}]
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


@app.route('/api/v1/users', methods=['GET'])
def list_of_users():
    # call the all_users() class method
    return jsonify({'users': User.all_users()})


@app.route('/api/v1/rides', methods=['POST'])
def create_ride():
    if (not request.json or
            "ride_id" not in request.json or
            "terms" not in request.json or
            "finish_date" not in request.json or
            "start_date" not in request.json or
            "free_spots" not in request.json or
            "contribution" not in request.json or
            'origin' not in request.json or
            'destination' not in request.json or
            "meet_point" not in request.json):

        return jsonify(
            {
                "error": "Bad request (400). The browser "
                         "(or proxy) sent a request "
                         "that this server could not understand."
            }
        )

    # origin, destination, meet_point, contribution, free_spots, start_date,
    # finish_date, terms
    origin = request.json['origin']
    destination = request.json['destination']
    meet_point = request.json['meet_point']
    contribution = request.json['contribution']
    free_spots = request.json['free_spots']
    start_date = request.json['start_date']
    finish_date = request.json['finish_date']
    terms = request.json['terms']
    ride_id = request.json['ride_id']

    # raise errors if ride_id is integer

    if not isinstance(ride_id, int):
        return jsonify({"error": "ride_id should be integer"})

    if not isinstance(terms, str):
        return jsonify({"error": "terms should be string"})

    if not isinstance(start_date, str):
        return jsonify({"error": "Start date should be string"})

    if not isinstance(finish_date, str):
        return jsonify({"error": "Finish date should be string"})

    if not isinstance(free_spots, int):
        return jsonify({"error": "Free spots should be integer"})

    if not isinstance(origin, str):
        return jsonify({"error": "Origin should be string"})

    if not isinstance(destination, str):
        return jsonify({"error": "Destination should be string"})

    if not isinstance(meet_point, str):
        return jsonify({"error": "meet_point should be string"})

    if not isinstance(contribution, (int, float, complex)):
        return jsonify({"error": "ride_id should be integer"})

    try:
        creating_user.offer_ride(
            origin,
            destination,
            meet_point,
            contribution,
            free_spots,
            start_date,
            finish_date,
            terms, ride_id
        )
    except:
        return jsonify(
            {"error": "Create account to create a ride or login"}
        )

    return jsonify({"rides": User.rides_list})


@app.route('/api/v1/rides', methods=['GET'])
def available_ride():
    # rides_list = [{"username_1": [{"origin": "", "destination": ""}]},
    # {"username_1": [{"origin": "", "destination
    # ": ""}]}]
    only_rides = []  # contains a dictionary of rides

    if len(User.rides_list) > 0:
        for dic in User.rides_list:
            for key in dic:  # capture username (key)
                for ride in dic[key]:  # loop through the value now
                    only_rides.append(ride)

        return jsonify(
            {"Rides": only_rides}
        )

    else:
        return jsonify(
            {"message": "No ride offers available, if you have a car create one !"}
        )


@app.route('/api/v1/rides/<ride_id>', methods=['GET'])
def get_single_ride(ride_id):

    # changing ride_id from type str to type int
    try:
        ride_id = int(ride_id)
    except:
        return jsonify(
            {"error": "ride_id should be of type integer"}
        )

    # if not isinstance(ride_id, int):
        # return jsonify({"error": "ride_id should be of type integer"})
    # rides_list = [{"username_1": [{"origin": "", "destination": ""}]},
    # {"username_1": [{"origin": "", "destination
    # ": ""}]}]

    count = 0
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
                                {"message": "The ride offer with ride_id {} does not exist".format(ride_id)}
                            )
                        else:
                            continue


# rides_list = [{"username_1": [{"origin": "", "destination": ""}]},
                        # {"username_1": [{"origin": "", "destination
    # ": ""}]}]

# rides_requests = [{ride_id: [{"username": ""}, {"username": ""}]},
# {ride_id: [{"username": ""}, {"username": ""}]}]
# Let users make request to join a ride offer
@app.route('/api/v1/rides/<ride_id>/requests', methods=['POST'])
def request_ride(ride_id):

        # changing ride_id from type str to type int
        try:
            ride_id = int(ride_id)
        except ValueError as exc:
            return jsonify(
                {"error": "ride_id should be of type integer. {}".format(str(exc))}
            )

        # if not isinstance(ride_id, int):
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
                                User.rides_request.append({ride_id: [{"username": creating_user.username}]})
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


@app.route('/api/v1/rides/requests', methods=['GET'])
def get_all_ride_requests():
    # all_requests = User.all_requests()
    return jsonify(
        {"Ride requests": User.all_requests()}
    )


if __name__ == '__main__':
    app.run(debug=True)
























































