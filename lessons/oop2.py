"""OOP part 2: classes and methods"""

# think of a class as a template
# it defines attributes and behaviors its objects will have

# obj are instances of a class
# if the class is the blueprint, the obj is the house
# the house has the specified attributes and behaviors of the class

# abstraction: whittling down to essentials
# ex: when u fly, do you need to know all the flight details (like how the pilot flies)
# or just the ones essential for me to know (departure time, seat assignment, etc.)

# objects are a data abstraction

# all obj have:
# 1. an internal representation (data attributes)
# 2. an interface for interacting with obj (interface defines behaviors but hides
# implementation) (methods: fn defined w/i a class, self is first parameter)

# methods are defined in the CLASS and used on OBJ


class Profile:
    username: str
    followers: list[str]
    following: list[str]

    def __init__(self, usr):
        self.username = usr
        self.followers = []
        self.following = []

    # Method definitions (first parameter is SELF)
    def follow(self, username: str) -> None:
        self.following.append(username)

    # Method definitions
    def get_following(self) -> list[str]:
        return self.following


my_prof: Profile = Profile("comp110fan")  # Calls __init__()
print(my_prof.following)
my_prof.follow("unc.latinosintech")  # method call <obj>,<method>(<non-SELF parameters>)
print(my_prof.following)


# class definition
class Point:
    x: float
    y: float

    # initializer/constructor
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # methods
    def dist_from_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def translate_x(self, dx: float) -> None:
        self.x += dx

    def translate_y(self, dy: float) -> None:
        self.y += dy


pt: Point = Point(2.0, 1.0)
