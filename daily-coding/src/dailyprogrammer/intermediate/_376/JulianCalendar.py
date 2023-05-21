# from challenge prompt
YEARS = [(2016, 2017), (2019, 2020), (1900, 1901), (2000, 2001),
         (2800, 2801), (123456, 123456), (1234, 5678), (123456, 7891011)]


def leaps(first, second):
    """Dependent on find_matches()
    Finds total number of revised julian calendar leap years between two years

    :param first: First year
    :param second: Second year
    :return: Revised julian calendar leap year amount between years
    :rtype: int
    """
    if first < 0 or second < 0:
        raise ValueError("Years must be positive")
    elif second < first:
        raise ValueError("Second year must be greater than equal to first")
    leaps4 = find_matches(first, second, 4, 0)
    exception100 = find_matches(first, second, 100, 0)
    leaps200 = find_matches(first, second, 900, 200)
    leaps600 = find_matches(first, second, 900, 600)
    total_leaps = leaps4 - exception100 + leaps200 + leaps600
    return total_leaps


def find_matches(first, second, divider, remainder):
    """Finds amt of years that match restrictions of divider, remainder
    The strategy here is to have first and second be cursors/pointers
    Adjust the cursors until both match with divider to make calculation of
    number of matches easier

    :param int first: First year
    :param int second: Second year
    :param int divider: The divisibility desired to be valid match
    :param int remainder: The remainder desired to be valid match
    :return: Number of matching years
    :rtype: int
    """
    # move first cursor to position
    while first % divider != remainder:
        first += 1
        if first == second:
            return 0
    # if two cursors are already in position
    if first % divider == remainder and second % divider == remainder:
        return (second - first) // divider
    # second cursor needs to be moved
    while second % divider != remainder:
        second -= 1
    return ((second - first) // divider) + 1


def main():
    # dev_only()
    for i in range(0, len(YEARS)):
        print('leaps' + str(YEARS[i]), '=>', leaps(YEARS[i][0], YEARS[i][1]))


def dev_only():
    """Used while developing, for testing
    Expect answer of 1, 2, 0 for all
    """
    # the leaps
    print('Dev4:')
    test4 = [(2000, 2004), (2001, 2009), (2001, 2004)]
    for i in range(0, len(test4)):
        print(test4[i], find_matches(test4[i][0], test4[i][1], 4, 0))
    # the exception
    print('Dev100:')
    test100 = [(2000, 2100), (2001, 2201), (2001, 2100)]
    for i in range(0, len(test100)):
        print(test100[i], find_matches(test100[i][0], test100[i][1], 100, 0))
    # exception to the exception (more leaps)
    print('Dev900_200:')
    test900_200 = [(1100, 2000), (1101, 2901), (1101, 1300)]
    for i in range(0, len(test900_200)):
        print(test900_200[i], find_matches(test900_200[i][0],
                                           test900_200[i][1], 900, 200))
    print('Dev900_600:')
    test900_600 = [(1500, 2400), (1501, 3301), (1501, 1700)]
    for i in range(0, len(test900_600)):
        print(test900_600[i], find_matches(test900_600[i][0],
                                           test900_600[i][1], 900, 600))


if __name__ == "__main__":
    main()

