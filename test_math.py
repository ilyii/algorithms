
def test_always_true():
    assert True


def test_euclids_algorithm(algorithm):
    # Test cases where one of the numbers is 0
    assert algorithm(0, 5) == 5
    assert algorithm(5, 0) == 5
    assert algorithm(0, 0) == 0

    # Test cases with positive integers
    assert algorithm(12, 18) == 6  # GCD of 12 and 18 is 6
    assert algorithm(48, 18) == 6  # GCD of 48 and 18 is 6
    assert algorithm(17, 5) == 1   # GCD of 17 and 5 is 1

    # Test cases with negative integers
    assert algorithm(-12, 18) == 6  # GCD of -12 and 18 is 6
    assert algorithm(12, -18) == 6  # GCD of 12 and -18 is 6
    assert algorithm(-12, -18) == 6 # GCD of -12 and -18 is 6

    # Test case with large numbers
    assert algorithm(123456789, 987654321) == 9  # GCD of these large numbers

    print("All test cases passed.")

