"""Object-Oriented Programming"""

# every object in python has:
# a type
# an internal data representation
# a set of precedures for interaction with the object

# an object is an instance of a type
# ex: 23 is an instance of an int


# declare a new data type with "class"
# lets model an instagram profile with a class
class Profile:
    username: str
    # declaring attributes of a class
    bio: str
    followers: int
    following: list[str]
    private: bool

    def __init__(self):
        # __init__ is a constructor that is called whenever a new instance of a class
        # is created. it is called each time a new instance is made
        # this initializes the attributes to a value
        self.username = "usr9"
        self.bio = ""
        self.followers = 0
        self.following = []
        self.private = False


# can use this new class to assign to a new data type
my_prof: Profile = Profile()
my_prof.username = "comp110fan"
print(my_prof.private)  # false
print(my_prof.followers)  # 0
my_prof.following.append(
    "unc"
)  # can change following to a list to update and keep track of who we follow
print(my_prof.following)  # [unc]
