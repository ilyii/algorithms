from math import euclids_algorithm
def test_always_true():
    assert True


def test_euclids_algorithm(euclids_algorithm):
    # Test cases where one of the numbers is 0
    assert euclids_algorithm(0, 5) == 5
    assert euclids_algorithm(5, 0) == 5
    assert euclids_algorithm(0, 0) == 0

    # Test cases with positive integers
    assert euclids_algorithm(12, 18) == 6  # GCD of 12 and 18 is 6
    assert euclids_algorithm(48, 18) == 6  # GCD of 48 and 18 is 6
    assert euclids_algorithm(17, 5) == 1   # GCD of 17 and 5 is 1

    # Test cases with negative integers
    assert euclids_algorithm(-12, 18) == 6  # GCD of -12 and 18 is 6
    assert euclids_algorithm(12, -18) == 6  # GCD of 12 and -18 is 6
    assert euclids_algorithm(-12, -18) == 6 # GCD of -12 and -18 is 6

    # Test case with large numbers
    assert euclids_algorithm(123456789, 987654321) == 9  # GCD of these large numbers

    print("All test cases passed.")

