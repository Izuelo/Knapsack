from itertools import groupby

from Knapsack import Knapsack

numberOfItems = 10
weightCapacity = 100  # total weight knapsack can hold
weightLower = 5  # lower boundary of randomized weight item can have
weightUpper = 25  # upper boundary of randomized weight item can have
valueLower = 7  # lower boundary of randomized value item can have
valueUpper = 46  # upper boundary of randomized value item can have
amountLower = 1  # lower boundary of how many times item can be selected
amountUpper = 7  # upper boundary of how many times item can be selected

test_case = ((1, 18, 22, 7),
             (2, 19, 14, 1),
             (3, 25, 45, 5),
             (4, 13, 37, 4),
             (5, 10, 36, 2),
             (6, 25, 28, 7),
             (7, 11, 40, 7),
             (8, 18, 10, 7),
             (9, 10, 27, 4),
             (10, 22, 10, 7))
all_tc = sum(([(id_name, wt, val)] * n for id_name, wt, val, n in test_case), [])

knapsack = Knapsack.Knapsack(weightCapacity, weightLower, weightUpper, valueLower, valueUpper, amountLower, amountUpper)
knapsack.generate(numberOfItems)

dp_table, bagged = knapsack.dp(all_tc)
print("Bagged (DP) the following %i items\n  " % len(bagged) +
      '\n  '.join('Amount of item \'%i\' = %s' % (item[0], len(list(grp)))
                  for item, grp in groupby(sorted(bagged))))
print("for a total value of %i and a total weight of %i" % (
    sum(item[2] for item in bagged), sum(item[1] for item in bagged)))

approx, total_val = knapsack.approx(all_tc)
print("Bagged (approx) the following %i items\n  " % len(approx) +
      '\n  '.join('Amount of item \'%i\' = %s' % (item[0], len(list(grp)))
                  for item, grp in groupby(sorted(approx))))
print("for a total value of %i and a total weight of %i" % (
    sum(item[2] * item[1] for item in approx), sum(item[1] for item in approx)))


