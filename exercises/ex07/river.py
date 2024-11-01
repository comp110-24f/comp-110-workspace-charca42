"""File to define River class."""

__author__ = "730391230"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Defines the River class."""

    day: int  # tells what day of the lifecycle im modeling
    fish: list[Fish]  # list of fish that stores fish population
    bears: list[Bear]  # list of bears that stores bear population

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the ages of the animals, and removes them if they are too old."""
        # if a fish age > 3, it is removed
        # if a bear age > 5, it is removed
        surv_bear: list[Bear] = []
        surv_fish: list[Fish] = []
        # add survivors to a new list rather than cycle thru and remove
        for fish in self.fish:
            if fish.age <= 3:
                surv_fish.append(fish)
        for bear in self.bears:
            if bear.age <= 5:
                surv_bear.append(bear)
        self.bears = surv_bear
        self.fish = surv_fish
        return None

    def bears_eating(self):
        """For each bear, if there are at least 5 fish, the bear eats 3 fish."""
        # uses remove_fish, calls eat() for the # of fish the bear eats
        for bear in self.bears:
            if len(self.fish) > 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        """Add surviving bears to a new list and copy it over."""
        # surv_bear is new list
        surv_bear: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score < 0:
                surv_bear.append(bear)
        self.bears = surv_bear
        return None

    def one_river_week(self):
        """Calls one_river_day 7 times."""
        count: int = 1
        while count <= 7:
            self.one_river_day()
            count += 1
        return None

    def remove_fish(self, amount: int):
        """Removes <amount> many Fish from the River."""
        idx = 0
        while idx < amount:
            self.fish.pop(idx)
            amount -= 1

    def repopulate_fish(self):
        """Simulates reproduction of the fish."""
        # each pair of fish produces 4 offspring (n//2 *4 new fish to add)
        # find the total number of fish to add, and make a looping cycle to append
        new_fish: int = (len(self.fish)) // 2 * 4
        idx: int = 1
        while idx <= new_fish:
            self.fish.append(Fish())
            idx += 1
        return None

    def repopulate_bears(self):
        """Simulates reproduction of the bears."""
        # each pair of bears will produce 1 offspring (for n bears, n//2 new bears)
        # find the total number of bears to add, and make a looping cycle to append
        new_bears: int = (len(self.bears)) // 2
        idx: int = 1
        while idx <= new_bears:
            self.bears.append(Bear())
            idx += 1
        return None

    def view_river(self):
        """Prints the status of the river."""
        # use an f string
        print(
            f"""
            ~~~ Day {self.day}: ~~~
            Fish population: {len(self.fish)}
            Bear population: {len(self.bears)}
            """
        )
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
