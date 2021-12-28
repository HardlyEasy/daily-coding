COINS = [500, 100, 25, 10, 5, 1]


def main():
    print('change(0) => ', change(0))
    print('change(12) => ', change(12))
    print('change(468) => ', change(468))
    print('change(123456) => ', change(123456))


def change(money):
    """ Returns number of coins used to make most efficient change from money

    :param int money: Fake currency units
    :return: Number of coins
    :rtype: int
    """
    change_list = []
    for i in range(0, len(COINS)):
        coin = COINS[i]  # start from highest coin
        coin_amt = money // coin
        leftover = money % coin
        change_list.append(coin_amt)
        money = leftover
    return sum(change_list)


if __name__ == "__main__":
    main()
