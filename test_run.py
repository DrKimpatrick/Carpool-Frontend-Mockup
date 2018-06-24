import unittest
import json
import run

BASE_URL = '/api/v1/'


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


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = run.app.test_client()
        self.app.testing = True

    # Testing APIs
    # users_list = [{"name":"", "email":"", "username":"", "phone_number":"", "bio":"", "gender":"", "password":""},
    #  {"name":"", "email":"", "username":"", "phone_number":"", "bio":"", "gender":"", "password":""}]
    def test_get_all_users(self):
        response = self.app.get('{}users'.format(BASE_URL))
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)

        # self.assertEqual(len(data['users']), 2)

    def test_create_user(self):
        # response = self.app.get('{}users'.format(BASE_URL))
        # data = json.loads(response.get_data())
        # self.assertEqual(response.status_code, 200)
        pass

    def test_login(self):
        pass

    def test_create_ride(self):
        ride = {"originc": "kampala", "destination": "Masaka", "meetpoint": "Ndeeba", "contribution": 5000,
         "free_spots": 4, "start_date": "21st/06/2018", "finish_date": "1st/06/2018", "terms": "terms", "rideId": 1000
         }
        # item = {"name": "some_item"}
        response = self.app.post(BASE_URL,
                                 data=json.dumps(ride),
                                 content_type='application/json')

        self.assertEqual(response.status_code, 404)

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

































