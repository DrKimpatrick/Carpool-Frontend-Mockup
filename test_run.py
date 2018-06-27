import unittest
import json
import sys
import run

BASE_URL = '/api/v1/'

"""
class TestUser(unittest.TestCase):
    def test_data_structures(self):
        self.assertIsInstance(run.User.rides_list, list)
        self.assertIsInstance(run.User.users_list, list)
        self.assertIsInstance(run.User.rides_request, list)
        self.assertIsInstance(run.User.accepted_request, list)

    def setUp(self):
        self.app = run.app
        self.client = self.app.test_client  # or self.app.test_client

        # name, email, username, phone_number, bio, gender, password
        new_user_1 = run.User("kimanje", "dr.kimanje2patrick2@gmail.com", "kimpatrick", 782957882, "this is kimpatrick",
                                "Male", "Kp15712Kp")

        new_user_1.signup()

        new_user_2 = run.User("kimanje_2", "dr.kimanje2patrick2@gmail.com_2", "kimpatrick_2", 782957882,
                            "this is kimpatrick", "Male_2", "Kp15712Kp_2")

        new_user_2.signup()

        new_user_3 = run.User("kimanje_3", "dr.kimanje2patrick2@gmail.com_3", "kimpatrick_3", 782957882,
                            "this is kimpatrick", "Male_3", "Kp15712Kp_3")

        new_user_3.signup()

        # origin, destination, meet_point, contribution, free_spots,
        # start_date, finish_date, terms, ride_id
        new_user_1.offer_ride("kampala", "masaka", "ndeeba", 5000, 45, "21st/06/2018", "1st/07/2018", "terms", 1000)
        new_user_1.offer_ride("kampala", "masaka", "ndeeba", 5000, 45, "21st/06/2018", "1st/07/2018", "terms", 2000)

    def test_created_user(self):

        for dic in run.User.users_list:
            self.assertIsInstance(dic, dict)

        # test the length of the list
        length = len(run.User.users_list)
        self.assertEqual(length, 3)

        # test first user and second user
        first_user = run.User.users_list[0]
        second_user = run.User.users_list[1]
        self.assertEqual(first_user['name'], "kimanje")
        self.assertEqual(first_user['password'], "Kp15712Kp")

        self.assertEqual(second_user['name'], "kimanje_2")
        self.assertEqual(second_user['password'], "Kp15712Kp_2")

    def test_offer_ride(self):
        # rides_list = [{"username_1": [{"origin": "", "destination": ""}]}]

        # one ride created hence is of length 1
        self.assertEqual(len(run.User.rides_list), 1)

        for dic in run.User.rides_list:
            for key in dic:
                self.assertEqual(key, "kimpatrick")
                self.assertIsInstance(dic[key], list)

                for ride in dic[key]:

                    # ride should be of type dictionary
                    self.assertIsInstance(ride, dict)

                    # ride dictionary should be aof length 9
                    self.assertEqual(len(ride), 9)

                    # check some dictionary values
                    self.assertEqual(ride['origin'], "kampala")
"""


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
        self.app = run.app.test_client()
        self.app.testing = True

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

    # Lets create only two users from the above data
    def test_create_user(self):

        # Creating a user instance, length is one
        response = self.app.post("{}users/signup".format(BASE_URL),
                                 data=json.dumps(self.user_1),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json['Users']), 1)

        # Username is unique, therefore an error message is raised here
        response = self.app.post("{}users/signup".format(BASE_URL),
                                 data=json.dumps(self.user_1),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json,
                         {"message": "Username already taken, try another"}
                         )
        self.assertEqual(response.json['message'],
                         "Username already taken, try another"
                         )

        # Second user instance | all expected to work fine
        response_2 = self.app.post("{}users/signup".format(BASE_URL),
                                   data=json.dumps(self.user_2),
                                   content_type='application/json')
        self.assertEqual(response_2.status_code, 200)
        self.assertEqual(len(response_2.json['Users']), 2)  # length=2

        # Wrong and missing user fields | Should raise and error message
        response_3 = self.app.post("{}users/signup".format(BASE_URL),
                                   data=json.dumps(self.user_3),
                                   content_type='application/json')
        self.assertEqual(response_3.status_code, 200)
        self.assertEqual(response_3.json['error'],
                         "Bad request (400). The browser (or proxy) sent a "
                         "request that this server could not understand."
                         )

    # Remember only two users were added to the users_list
    def test_get_all_users(self):
        response = self.app.get('{}users'.format(BASE_URL))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json['Users']), 2)

    def test_login(self):
        pass

    def test_create_ride(self):
        ride = {"origin": "kampala",
                "destination": "Masaka",
                "meet_point": "Ndeeba",
                "contribution": 5000,
                "free_spots": 4,
                "start_date": "21st/06/2018",
                "finish_date": "1st/06/2018",
                "terms": "terms", "ride_id": 1000}

        # item = {"name": "some_item"}
        response = self.app.post(BASE_URL,
                                 data=json.dumps(ride),
                                 content_type='application/json')

        self.assertEqual(response.status_code, 404)

        response = self.app.post("{}rides".format(BASE_URL),
                                 data=json.dumps(ride),
                                 content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"error": "Create account to create a ride or login"})

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

































