from itertools import groupby

from Knapsack import Knapsack

numberOfItems = 1000
weightCapacity = 400  # total weight knapsack can hold
weightLower = 1  # lower boundary of randomized weight item can have
weightUpper = 20  # upper boundary of randomized weight item can have
valueLower = 1  # lower boundary of randomized value item can have
valueUpper = 60  # upper boundary of randomized value item can have
amountLower = 1  # lower boundary of how many times item can be selected
amountUpper = 4  # upper boundary of how many times item can be selected

knapsack = Knapsack.Knapsack(weightCapacity, weightLower, weightUpper, valueLower, valueUpper, amountLower,
                             amountUpper)


def testCase():
    test_knapsack = Knapsack.Knapsack(50, weightLower, weightUpper, valueLower, valueUpper, amountLower,
                                      amountUpper)

    test_case = ((1, 5, 16, 4),
                 (2, 2, 6, 4),
                 (3, 4, 3, 4),
                 (4, 4, 4, 2),
                 (5, 1, 11, 2),
                 (6, 4, 18, 2),
                 (7, 6, 19, 1),
                 (8, 7, 6, 3),
                 (9, 1, 4, 2),
                 (10, 6, 18, 2))
    all_tc = sum(([(id_name, wt, val)] * n for id_name, wt, val, n in test_case), [])

    # DP
    dp_table, bagged = test_knapsack.dp(all_tc)

    # Approx
    app_table, app_value = test_knapsack.approx(all_tc)
    printResult(bagged, app_table, 10)


def findDiff():
    find = True
    while find:
        gen_items, raw_gen = knapsack.generate(numberOfItems)

        dp_table, bagged = knapsack.dp(gen_items)
        dp_value = sum(item[2] for item in bagged)

        app_table, app_value = knapsack.approx(gen_items)

        if sum(item[1] for item in app_table) == sum(item[1] for item in bagged) and app_value != dp_value:
            print("----Generated items----")
            print(raw_gen)
            printResult(bagged, app_table, numberOfItems)
            find = False


def printResult(dp, approx, numOfItems):
    print("Bagged (DP) the following %i items\n  " % len(dp) +
          ' -- '.join('\'%i\' = %s' % (item[0], len(list(grp)))
                      for item, grp in groupby(sorted(dp))))

    value_dp = sum(item[2] for item in dp), sum(item[1] for item in dp)

    print("for a total value of %i and a total weight of %i" % (value_dp[0], value_dp[1]))

    print("Bagged (approx) the following %i items\n  " % len(approx) +
          ' -- '.join('\'%i\' = %s' % (item[0], len(list(grp)))
                      for item, grp in groupby(sorted(approx))))
    value_app = sum(item[2] * item[1] for item in approx), sum(item[1] for item in approx)
    print("for a total value of %i and a total weight of %i" % (value_app[0], value_app[1]))

    relative_error = (abs(value_dp[0] - value_app[0]) / value_dp[0]) * 100
    print("Relative error of knapsack value: " + str(relative_error) + "%")

    dp_group = [(item[0], len(list(grp))) for item, grp in groupby(sorted(dp))]
    approx_group = [(item[0], len(list(grp))) for item, grp in groupby(sorted(approx))]

    res = []
    dp_diff = []
    approx_diff = []

    for x in range(1, numOfItems + 1):
        dp_item = [i for i in dp_group if i[0] == x]
        approx_item = [i for i in approx_group if i[0] == x]

        if dp_item or approx_item:
            if dp_item and approx_item and dp_item[0][1] != approx_item[0][1]:
                res.append((x, abs(dp_item[0][1] - approx_item[0][1])))
                if dp_item[0][1] > approx_item[0][1]:
                    dp_diff.append((x, dp_item[0][1] - approx_item[0][1]))
                else:
                    approx_diff.append((x, approx_item[0][1] - dp_item[0][1]))
            elif dp_item and not approx_item:
                res.append(dp_item[0])
                dp_diff.append(dp_item[0])
            elif approx_item and not dp_item:
                res.append(approx_item[0])
                approx_diff.append(approx_item[0])
    print("Symmetric difference between Approx and DP algorithms:")
    print(res)
    print("Difference DP - Approx :")
    print(dp_diff)
    print("Difference Approx - DP :")
    print(approx_diff)


testCase()
