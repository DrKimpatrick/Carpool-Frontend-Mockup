class User(object):
    """ Creates a user instance and links the user to all activities done
    by that user e.g creating a ride offer and requesting for a ride """

    users_list = []  # users_list = [{"name":"", "email":"", "username":""]

    rides_list = []  # rides_list = ["username": [{}, {}, {}]]

    rides_request = []  # list of ride requests
    accepted_request = []  # list of accepted requests (rides taken)

    def __init__(self,
                 name,
                 email,
                 username,
                 phone_number,
                 bio,
                 gender,
                 password):
        self.name = name
        self.username = username
        self.email = email
        self.phone_number = phone_number
        self.bio = bio
        self.gender = gender
        self.password = password
        self.new_user = {}

    def signup(self):
        """ Is called from the view (create_user) to create a user """
        self.new_user['name'] = self.name
        self.new_user['email'] = self.email
        self.new_user['username'] = self.username
        self.new_user['phone_number'] = self.phone_number
        self.new_user['bio'] = self.bio
        self.new_user['gender'] = self.gender
        self.new_user['password'] = self.password

        # now append the new dictionary to the User list
        self.users_list.append(self.new_user)

    """ Is called from the view to create a ride offer """
    def offer_ride(self,
                   origin,
                   destination,
                   meet_point,
                   contribution,
                   free_spots,
                   start_date,
                   finish_date,
                   terms,
                   ride_id):

        # initialising an empty dict
        ride_dict = {}

        ride_dict['origin'] = origin
        ride_dict['destination'] = destination
        ride_dict['meet_point'] = meet_point
        ride_dict['contribution'] = contribution
        ride_dict['free_spots'] = free_spots
        ride_dict['start_date'] = start_date
        ride_dict['finish_date'] = finish_date
        ride_dict['terms'] = terms
        ride_dict['ride_id'] = ride_id

        count = 0
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
        """ Returns all ride requests available """
        if len(User.rides_request) < 1:
            return "No rides requests available"
        else:
            return cls.rides_request

    @classmethod
    def all_users(cls):
        """ Returns all created users """
        if len(User.users_list) < 1:
            return "No user accounts available"
        else:
            return cls.users_list
