class User(object):
    # users_list = [
    # {"name":"", "email":"", "username":"", "phone_number":"",
    #  "bio":"", "gender":"", "password":""},
    #  {"name":"", "email":"", "username":"", "phone_number":"",
    # "bio":"", "gender":"", "password":""}]

    users_list = []  # list of all application users

    # rides_list = ["username": [{}, {}, {}], "username": [{}, {}, {}]]
    rides_list = []  # lists all available ride offers

    rides_request = []  # list of ride requests
    accepted_request = []  # list of accepted requests (rides taken)

    def __init__(
            self,
            name,
            email,
            username,
            phone_number,
            bio,
            gender,
            password
    ):
        self.name = name
        self.username = username
        self.email = email
        self.phone_number = phone_number
        self.bio = bio
        self.gender = gender
        self.password = password
        self.new_user = {}

    def signup(self):
        self.new_user['name'] = self.name
        self.new_user['email'] = self.email
        self.new_user['username'] = self.username
        self.new_user['phone_number'] = self.phone_number
        self.new_user['bio'] = self.bio
        self.new_user['gender'] = self.gender
        self.new_user['password'] = self.password

        # now append the new dictionary to the User list
        self.users_list.append(self.new_user)

    def offer_ride(
            self,
            origin,
            destination,
            meet_point,
            contribution,
            free_spots,
            start_date,
            finish_date,
            terms,
            rideId
    ):
        # rides_list = [{"username_1": [{"origin": "", "destination": ""}]}]
        ride_dict = {}

        ride_dict['origin'] = origin
        ride_dict['destination'] = destination
        ride_dict['meet_point'] = meet_point
        ride_dict['contribution'] = contribution
        ride_dict['free_spots'] = free_spots
        ride_dict['start_date'] = start_date
        ride_dict['finish_date'] = finish_date
        ride_dict['terms'] = terms
        ride_dict['rideId'] = rideId

        count = 0
        # rides_list = [{"username_1": [{"origin": "", "destination": ""}]}]
        if len(self.rides_list) < 1:
            # if the rides_list is empty
            self.rides_list.append(
                {self.username: [ride_dict]}
            )
            return
        else:
            for dic in self.rides_list:
                count += 1
                for key in dic:
                    if key != self.username:
                        # if the rides_list is not empty and the current user
                        # does not have any ride offer
                        if len(self.rides_list) == count:
                            # dic[self.username] = [ride_dict]  #
                            # create a dictionary in a list
                            self.rides_list.append(
                                {self.username: [ride_dict]}
                            )
                            return
                        else:
                            continue
                    else:
                        dic[key].append(ride_dict)
                        return

    @classmethod
    def all_requests(cls):
        if len(User.rides_request) < 1:
            return "No rides requests available"
        else:
            return cls.rides_request

    @classmethod
    def all_users(cls):
        if len(User.users_list) < 1:
            return "No user accounts available"
        else:
            return cls.users_list
