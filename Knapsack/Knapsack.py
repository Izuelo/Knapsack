import random
import numpy as np


class Knapsack:
    weightCapacity = 0  # total weight knapsack can hold
    weightLower = 0  # lower boundary of randomized weight item can have
    weightUpper = 0  # upper boundary of randomized weight item can have
    valueLower = 0  # lower boundary of randomized value item can have
    valueUpper = 0  # upper boundary of randomized value item can have
    amountLower = 0  # lower boundary of how many times item can be selected
    amountUpper = 0  # upper boundary of how many times item can be selected

    generatedItems = ()

    def __init__(self, weightCapacity: int, weightLower: int, weightUpper: int, valueLower: int, valueUpper: int,
                 amountLower: int, amountUpper: int):
        self.weightCapacity = weightCapacity
        self.weightLower = weightLower
        self.weightUpper = weightUpper
        self.valueLower = valueLower
        self.valueUpper = valueUpper
        self.amountLower = amountLower
        self.amountUpper = amountUpper

    def generate(self, number_of_things: int):
        all_items = ()
        for i in range(1, number_of_things + 1):
            item = (i,
                    random.randint(self.weightLower, self.weightUpper),
                    random.randint(self.valueLower, self.valueUpper),
                    random.randint(self.amountLower, self.amountUpper))
            all_items += (item,)
        self.generatedItems = all_items
        return sum(([(id_name, wt, val)] * n for id_name, wt, val, n in self.generatedItems), [])

    def dp(self, items):
        operation_counter = 0
        limit = self.weightCapacity
        table = np.zeros((len(items) + 1, limit + 1))

        for j in range(1, len(items) + 1):
            id_name, wt, val = items[j - 1]
            operation_counter += 1
            for w in range(1, limit + 1):
                if wt > w:
                    table[j][w] = table[j - 1][w]
                    operation_counter += 1
                else:
                    table[j][w] = max(table[j - 1][w],
                                      table[j - 1][w - wt] + val)
                    operation_counter += 1

        result = []
        w = limit
        for j in range(len(items), 0, -1):
            operation_counter += 1
            if table[j][w] != table[j - 1][w]:
                item, wt, val = items[j - 1]
                result.append(items[j - 1])
                w -= wt

        print("--DP--")
        print("Value: %i \n Weight: %i" % (
            sum(item[2] for item in result), sum(item[1] for item in result)))
        return table, result

    def approx(self, items):
        operation_counter = 0
        items_approx = np.array(items.copy())
        items_approx = [list(elem) for elem in items_approx]
        for item in items_approx:
            item[2] = item[2] / item[1]
            operation_counter += 1
        items_approx.sort(key=lambda itemT: itemT[2], reverse=True)
        # items_approx = np.array(items_approx)
        approx_result = []
        current_weight = 0
        current_value = 0
        for i in range(len(items_approx)):
            operation_counter += 1
            if items_approx[i][1] + current_weight <= self.weightCapacity:
                approx_result += (items_approx[i],)
                current_weight += items_approx[i][1]
                current_value += items_approx[i][2] * items_approx[i][1]

        print("--Approximation--")
        print("Value: " + str(current_value) + " \n Weight: " + str(current_weight))
        return approx_result, current_value
