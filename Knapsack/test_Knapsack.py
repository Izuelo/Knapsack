from unittest import TestCase
from Knapsack import Knapsack


# probably that's not how you should write a test

class TestKnapsack(TestCase):
    weightLower = 50  # lower boundary of randomized weight item can have
    weightUpper = 100  # upper boundary of randomized weight item can have
    valueLower = 7  # lower boundary of randomized value item can have
    valueUpper = 87  # upper boundary of randomized value item can have
    amountLower = 1  # lower boundary of how many times item can be selected
    amountUpper = 4  # upper boundary of how many times item can be selected
    s = 400

    knapsack = Knapsack(s, weightLower, weightUpper, valueLower, valueUpper, amountLower, amountUpper)

    items_for10 = knapsack.generate(10)
    items_for100 = knapsack.generate(100)
    items_for1000 = knapsack.generate(1000)
    items_for2000 = knapsack.generate(2000)

    def test_for_10dp(self):
        print("10 DP")
        self.knapsack.dp(self.items_for10)

    def test_for_100dp(self):
        print("100 DP")
        self.knapsack.dp(self.items_for100)

    def test_for_1000dp(self):
        print("1000 DP")
        self.knapsack.dp(self.items_for1000)

    def test_for_2000dp(self):
        print("2000 DP")
        self.knapsack.dp(self.items_for2000)

    def test_for_10approx(self):
        print("10 approx")
        self.knapsack.approx(self.items_for10)

    def test_for_100approx(self):
        print("100 approx")

        self.knapsack.approx(self.items_for100)

    def test_for_1000approx(self):
        print("1000 approx")
        self.knapsack.approx(self.items_for1000)

    def test_for_2000approx(self):
        print("2000 approx")
        self.knapsack.approx(self.items_for2000)
