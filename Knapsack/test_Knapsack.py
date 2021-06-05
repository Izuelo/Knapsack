from unittest import TestCase
from Knapsack.Knapsack import Knapsack


# probably that's not how you should write a test

class TestKnapsack(TestCase):
    weightLower = 5  # lower boundary of randomized weight item can have
    weightUpper = 25  # upper boundary of randomized weight item can have
    valueLower = 7  # lower boundary of randomized value item can have
    valueUpper = 46  # upper boundary of randomized value item can have
    amountLower = 1  # lower boundary of how many times item can be selected
    amountUpper = 7  # upper boundary of how many times item can be selected

    knapsack10 = Knapsack(10, weightLower, weightUpper, valueLower, valueUpper, amountLower, amountUpper)
    knapsack100 = Knapsack(100, weightLower, weightUpper, valueLower, valueUpper, amountLower, amountUpper)
    knapsack1000 = Knapsack(1000, weightLower, weightUpper, valueLower, valueUpper, amountLower, amountUpper)
    knapsack2000 = Knapsack(1000, weightLower, weightUpper, valueLower, valueUpper, amountLower, amountUpper)
    items_for10 = knapsack10.generate(10)
    items_for100 = knapsack100.generate(100)
    items_for1000 = knapsack1000.generate(1000)
    items_for2000 = knapsack2000.generate(2000)

    def test_for_10dp(self):
        self.knapsack10.dp(self.knapsack10.items)

    def test_for_100dp(self):
        self.knapsack100.dp(self.knapsack100.items)

    def test_for_1000dp(self):
        self.knapsack1000.dp(self.knapsack1000.items)

    def test_for_2000dp(self):
        self.knapsack2000.dp(self.knapsack2000.items)

    def test_for_10approx(self):
        self.knapsack10.approx(self.knapsack10.items)

    def test_for_100approx(self):
        self.knapsack100.approx(self.knapsack100.items)

    def test_for_1000approx(self):
        self.knapsack1000.approx(self.knapsack1000.items)

    def test_for_2000approx(self):
        self.knapsack2000.approx(self.knapsack2000.items)
