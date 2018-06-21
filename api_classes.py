class User(object):
    # users_list = [{"name":"", "email":"", "username":"", "phone_number":"", "bio":"", "gender":"", "password":""},
    #  {"name":"", "email":"", "username":"", "phone_number":"", "bio":"", "gender":"", "password":""}]
    users_list = []  # list of all application users

    # rides_list = ["username": [{}, {}, {}], "username": [{}, {}, {}]]
    rides_list = []  # lists all available ride offers

    request = []  # list of ride requests
    accepted_request = []  # list of accepted requests (rides taken)

    def __init__(self, name, email, username, phone_number, bio, gender, password):
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































