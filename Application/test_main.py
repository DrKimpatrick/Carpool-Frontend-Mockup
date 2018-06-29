import unittest
import json
from Application import models
from Application import views


BASE_URL = '/api/v1/'
content_type = 'application/json'


class TestFlaskApi(unittest.TestCase):
    """
            ========== Revision Notes ===========
            response.json = {"key": "value"}
            if key = User and Value = [{}]
            response.json['User'] = [{}]

            The key depends on the returned json "key"
            return jsonify("message": "some message")
            return jsonify("error": "some message")
            """

    def setUp(self):
        self.app = views.app.test_client()
        self.app.testing = True
        self.user_object = models.User

        # --------***** Creating users ********------------------

        # second user instance
        self.user_1 = {
            "name": "patrick",
            "email": "dr.kimpatrick@gmail.com",
            "username": "kimpatrick",
            "phone_number": "078127364",
            "bio": "This is patrick, mum's last born",
            "gender": "Male",
            "password": "Kp15712Kp"
        }

        # second user instance
        self.user_2 = {
            "name": "patrick",
            "email": "dr.kimpatrick@gmail.com",
            "username": "kimpatrick_2",
            "phone_number": "078127364",
            "bio": "This is patrick, mum's last born",
            "gender": "Male",
            "password": "Kp15712Kp"
        }

        # wrong and missing parameters
        self.user_3 = {
            "name_3": "patrick",
            "email": "dr.kimpatrick@gmail.com",
            "username_3": "kimpatrick_3",
            "bio": "This is patrick, mum's last born",
            "gender_3": "Male",
            "password": "Kp15712Kp"
        }

        # ---------------- Testing the user login --------------------

        # This user exists
        self.login_user_1 = {
            "username": "kimpatrick",
            "password": "Kp15712Kp"
        }

        # This user does not exist
        self.login_user_404 = {
            "username": "kimpatrick_404",
            "password": "Kp15712Kp"
        }

        # Bad request 400 | wrong inputs (keys)
        self.login_user_400 = {
            "username_400": "kimpatrick_400",
            "password": "Kp15712Kp"
        }

        # ----------------- Create ride offers ---------------------

        self.ride_1 = {"origin": "kampala",
                       "destination": "Masaka",
                       "meet_point": "Ndeeba",
                       "contribution": 5000,
                       "free_spots": 4,
                       "start_date": "21st/06/2018",
                       "finish_date": "1st/06/2018",
                       "terms": "terms",
                       "ride_id": 1000}

        self.ride_2 = {"origin": "Busabala",
                       "destination": "Kampala",
                       "meet_point": "Ndeeba",
                       "contribution": 6000,
                       "free_spots": 5,
                       "start_date": "21st/06/2018",
                       "finish_date": "1st/06/2018",
                       "terms": "terms",
                       "ride_id": 2000}

        self.ride_400 = {"origin_400": "Busabala",
                         "destination_400": "Kampala",
                         "meet_point": "Ndeeba",
                         "contribution": 6000,
                         "free_spots": 9,
                         "start_date": "21st/06/2018",
                         "finish_date": "1st/06/2018",
                         "terms": "terms",
                         "ride_id": 3000}

    """ Lets create only two users from the above data """

    def test_create_user_1(self):

        # Creating a user instance, length is one
        response = self.app.post("{}users/signup".format(BASE_URL),
                                 data=json.dumps(self.user_1),
                                 content_type=content_type)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json['Users']), 1)

    def test_create_user_2(self):
        """ Has the same username with the created user above """

        # Username is unique, therefore an error message is raised here
        response = self.app.post("{}users/signup".format(BASE_URL),
                                 data=json.dumps(self.user_1),
                                 content_type=content_type)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json,
                         {"message": "Username already taken, try another"}
                         )
        self.assertEqual(response.json['message'],
                         "Username already taken, try another"
                         )

    def test_create_user_3(self):
        """ Second user instance | all expected to work fine """
        response_2 = self.app.post("{}users/signup".format(BASE_URL),
                                   data=json.dumps(self.user_2),
                                   content_type=content_type)
        self.assertEqual(response_2.status_code, 200)
        self.assertEqual(len(response_2.json['Users']), 2)  # length=2

    def test_create_user_4(self):
        """ Wrong and missing user fields | Should raise and error message """
        response_3 = self.app.post("{}users/signup".format(BASE_URL),
                                   data=json.dumps(self.user_3),
                                   content_type=content_type)
        self.assertEqual(response_3.status_code, 400)
        self.assertEqual(response_3.json, {"error": "You have either missed out some info or used wrong keys"})

    def test_get_all_users(self):
        """ Remember only two users were added to the users_list """

        response = self.app.get('{}users'.format(BASE_URL))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json['Users']), len(models.User.users_list))
        self.assertEqual(response.json['Users'], models.User.users_list)

    # ------------- Test the login route -------------------------------

    def test_login_1(self):

        # ---- for bad request ---------------------------
        response_400 = self.app.post("{}users/login".format(BASE_URL),
                                     data=json.dumps(self.login_user_400),
                                     content_type=content_type)
        self.assertEqual(response_400.status_code, 400)

    def test_login_2(self):
        """ Right data """
        response_1 = self.app.post("{}users/login".format(BASE_URL),
                                   data=json.dumps(self.login_user_1),
                                   content_type=content_type)

        self.assertEqual(response_1.status_code, 200)
        self.assertEqual(response_1.json, {"message": "You are logged in"})
        self.assertEqual(response_1.json['message'], "You are logged in")

    def test_login_3(self):
        """ Right data but username does not exist """
        response_404 = self.app.post("{}users/login".format(BASE_URL),
                                     data=json.dumps(self.login_user_404),
                                     content_type=content_type)

        self.assertEqual(response_404.json,
                         {"message": "Your username or password is incorrect"})

        self.assertEqual(response_404.json['message'],
                         "Your username or password is incorrect")

    def test_create_ride(self):
        """ wrong data | missing data or keys """

        response_400 = self.app.post('{}rides'.format(BASE_URL),
                                     data=json.dumps(self.ride_400),
                                     content_type=content_type)
        self.assertEqual(response_400.status_code, 400)
        self.assertEqual(response_400.json, None)

    def test_available_ride(self):
        pass

    def test_get_single_ride(self):
        pass

    def test_get_user_rides(self):
        pass

    def test_available_requests(self):
        pass

    def test_request_ride(self):
        pass

































