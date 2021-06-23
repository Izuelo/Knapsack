from unittest import TestCase
from Knapsack import Knapsack


class TestKnapsackTwo(TestCase):
    weightLower = 5  # lower boundary of randomized weight item can have
    weightUpper = 80  # upper boundary of randomized weight item can have
    valueLower = 30  # lower boundary of randomized value item can have
    valueUpper = 210  # upper boundary of randomized value item can have
    amountLower = 1  # lower boundary of how many times item can be selected
    amountUpper = 4  # upper boundary of how many times item can be selected

    knapsack50 = Knapsack(50, weightLower, weightUpper, valueLower, valueUpper, amountLower, amountUpper)
    knapsack100 = Knapsack(100, weightLower, weightUpper, valueLower, valueUpper, amountLower, amountUpper)
    knapsack200 = Knapsack(200, weightLower, weightUpper, valueLower, valueUpper, amountLower, amountUpper)
    knapsack500 = Knapsack(500, weightLower, weightUpper, valueLower, valueUpper, amountLower, amountUpper)
    knapsack700 = Knapsack(700, weightLower, weightUpper, valueLower, valueUpper, amountLower, amountUpper)
    knapsack1000 = Knapsack(1000, weightLower, weightUpper, valueLower, valueUpper, amountLower, amountUpper)

    items_for1000 = knapsack50.generate(1000)

    def test_for_knapsack50(self):
        print("50 KNAPSACK APP")
        self.knapsack50.approx(self.items_for1000)

    def test_for_knapsack100(self):
        print("100 KNAPSACK APP")
        self.knapsack100.approx(self.items_for1000)

    def test_for_knapsack200(self):
        print("200 KNAPSACK APP")
        self.knapsack200.approx(self.items_for1000)

    def test_for_knapsack500(self):
        print("500 KNAPSACK APP")
        self.knapsack500.approx(self.items_for1000)

    def test_for_knapsack700(self):
        print("700 KNAPSACK APP")
        self.knapsack700.approx(self.items_for1000)

    def test_for_knapsack1000(self):
        print("1000 KNAPSACK APP")
        self.knapsack1000.approx(self.items_for1000)

    def test_for_knapsack50dp(self):
        print("50 KNAPSACK DP")
        self.knapsack50.dp(self.items_for1000)

    def test_for_knapsack100dp(self):
        print("100 KNAPSACK DP")
        self.knapsack100.dp(self.items_for1000)

    def test_for_knapsack200dp(self):
        print("200 KNAPSACK DP")
        self.knapsack200.dp(self.items_for1000)

    def test_for_knapsack500dp(self):
        print("500 KNAPSACK DP")
        self.knapsack500.dp(self.items_for1000)

    def test_for_knapsack700dp(self):
        print("700 KNAPSACK DP")
        self.knapsack700.dp(self.items_for1000)

    def test_for_knapsack1000dp(self):
        print("1000 KNAPSACK DP")
        self.knapsack1000.dp(self.items_for1000)
