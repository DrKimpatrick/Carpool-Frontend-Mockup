from flask import Flask, request, jsonify, abort, make_response
from Application.models import User

app = Flask(__name__)


@app.route('/api/v1/users/signup', methods=['POST'])
def create_user():
    """ Creating a user. users_list = [{"username":"", "name":""}]"""

    if (not request.json or
            "name" not in request.json or
            "email" not in request.json or
            "username" not in request.json or
            "phone_number" not in request.json or
            "bio" not in request.json or
            "gender" not in request.json or
            "password" not in request.json):

        return jsonify(
            {"error": "You have either missed out some info or used wrong keys"}
        ), 400

    name = request.json["name"]
    email = request.json['email']
    username = request.json['username']
    phone_number = request.json['phone_number']
    bio = request.json['bio']
    gender = request.json['gender']
    password = request.json['password']

    for user in User.users_list:
        # username already exists
        if user['username'] == request.json['username']:
            return jsonify(
                {"message": "Username already taken, try another"}
            )
    else:
        global creating_user
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


@app.route('/api/v1/users', methods=['GET'])
def list_of_users():
    """ Get all users, all_users() is defined in the User class"""
    return jsonify({'Users': User.all_users()})


@app.route('/api/v1/users/login', methods=['POST'])
def login():
    """ The function confirms the presence of user. It does not login the user """

    if (not request.json or
            "username" not in request.json or
            "password" not in request.json):

            abort(400)

    username = request.json['username']
    password = request.json['password']

    # Check whether user exists
    for user in User.users_list:
        if user['username'] == username and user['password'] == password:
            return jsonify({"message": "You are logged in"})
    else:
        return jsonify(
            {"message": "Your username or password is incorrect"}
        )


@app.route('/api/v1/rides', methods=['POST'])
def create_ride():
    """ Creating a ride offer """

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
            {"error": "You have either missed out some info or used wrong keys"}
        ), 400

    origin = request.json['origin']
    destination = request.json['destination']
    meet_point = request.json['meet_point']
    contribution = request.json['contribution']
    free_spots = request.json['free_spots']
    start_date = request.json['start_date']
    finish_date = request.json['finish_date']
    terms = request.json['terms']
    ride_id = request.json['ride_id']

    # Checking for errors

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

    # ensuring that ride_id is unique
    for users_rides in User.rides_list:
        for username in users_rides:
            for ride in users_rides[username]:
                if ride['ride_id'] == ride_id:
                    return jsonify({"message": "Ride with a same ride_id {} exists, choose another".format(ride_id)})
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
    except Exception as e:
        response = {
            'message': str(e) + ", try to sign up"
        }

        return make_response(jsonify(response)), 401

    return jsonify({"Rides": User.rides_list[-1]})


@app.route('/api/v1/rides', methods=['GET'])
def available_ride():
    """ Retrieves all the available ride offers
    rides_list = [{"username_1": [{"origin": "", "destination": ""} """

    only_rides = []  # contains a dictionary of rides

    if len(User.rides_list) > 0:
        for dic_in_list in User.rides_list:
            for username in dic_in_list:  # capture username (key)
                for ride in dic_in_list[username]:  # loop through the value now
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
    """ Retrieve a single ride by providing the ride_id """

    # changing ride_id from type str to type int
    try:
        ride_id = int(ride_id)
    except Exception as e:
        return jsonify(
            {"error": str(e)+", ride_id should be of type integer"}
        )

    # Check for that ride_id
    for users_rides in User.rides_list:
        for username in users_rides:
            for ride in users_rides[username]:
                if int(ride['ride_id']) == ride_id:
                    return jsonify(
                        {"Ride": ride}
                    )
    else:
        return jsonify(
            {"message":
             "The ride offer with ride_id {} does not exist".format(ride_id)}
        )


@app.route('/api/v1/rides/<ride_id>/requests', methods=['POST'])
def request_ride(ride_id):
        """ Passenger can request for a ride by providing the ride_id"""

        try:
            ride_id = int(ride_id)
        except ValueError as exc:
            return jsonify(
                {"error": "ride_id should be of type integer. {}".format(str(exc))}
            )

        # Check for that ride_id
        for users_rides in User.rides_list:
            for username in users_rides:
                for ride in users_rides[username]:
                    if int(ride['ride_id']) == ride_id:

                        if username == creating_user.username:
                            return jsonify({"message": "You can not make a request to your ride"})

                        for ride_request in User.rides_request:
                            for key_as_ride_id in ride_request:
                                if int(key_as_ride_id) == ride_id:

                                    # A user should send a request to a ride once
                                    for user_as_dict in ride_request[key_as_ride_id]:
                                        if user_as_dict['username'] == creating_user.username:
                                            return jsonify(
                                                {"message":
                                                 "You already requested for this ride, just be patient"})
                                    else:
                                        ride_request[key_as_ride_id].append({"username": creating_user.username})
                                        return jsonify(
                                            {"message":
                                             "Ride request successfully sent and is pending approval"})
                        else:
                            User.rides_request.append({ride_id: [{"username": creating_user.username}]})
                            return jsonify({"message": "Ride request successfully sent and is pending approval"})

        else:
            return jsonify(
                {"message":
                 "The ride offer with ride_id {} does not exist".format(ride_id)}
            )


@app.route('/api/v1/rides/requests', methods=['GET'])
def get_all_ride_requests():
    """ Returns all the ride requests """

    return jsonify(
        {"Ride requests": User.all_requests()}
    )























































