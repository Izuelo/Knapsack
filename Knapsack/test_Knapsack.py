from unittest import TestCase
from Knapsack import Knapsack


class TestKnapsack(TestCase):
    weightLower = 20  # lower boundary of randomized weight item can have
    weightUpper = 100  # upper boundary of randomized weight item can have
    valueLower = 7  # lower boundary of randomized value item can have
    valueUpper = 67  # upper boundary of randomized value item can have
    amountLower = 1  # lower boundary of how many times item can be selected
    amountUpper = 4  # upper boundary of how many times item can be selected
    s = 100

    knapsack = Knapsack(s, weightLower, weightUpper, valueLower, valueUpper, amountLower, amountUpper)

    items_for10, t = knapsack.generate(10)
    items_for100, t = knapsack.generate(100)
    items_for1000, t = knapsack.generate(1000)
    items_for5000, t = knapsack.generate(5000)
    items_for10000, t = knapsack.generate(10000)

    def test_for_10dp(self):
        print("10 DP")
        self.knapsack.dp(self.items_for10)

    def test_for_100dp(self):
        print("100 DP")
        self.knapsack.dp(self.items_for100)

    def test_for_1000dp(self):
        print("1000 DP")
        self.knapsack.dp(self.items_for1000)

    def test_for_5000dp(self):
        print("5000 DP\n\n")
        self.knapsack.dp(self.items_for5000)

    def test_for_10000dp(self):
        print("10000 DP\n\n")
        self.knapsack.dp(self.items_for10000)

    def test_for_10approx(self):
        print("10 approx")
        self.knapsack.approx(self.items_for10)

    def test_for_100approx(self):
        print("100 approx")

        self.knapsack.approx(self.items_for100)

    def test_for_1000approx(self):
        print("1000 approx")
        self.knapsack.approx(self.items_for1000)

    def test_for_5000approx(self):
        print("5000 approx")
        self.knapsack.approx(self.items_for5000)

    def test_for_10000approx(self):
        print("10000 approx")
        self.knapsack.approx(self.items_for10000)
