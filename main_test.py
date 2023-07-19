"""
Module name: main_tests
Description: Module where we keep tests for individual functions.
Author: Kacper Turek
Date: 2023-07-18
"""

from unittest.mock import patch
import main_function as mf


def test_user_lotto_numbers():
    """
    Testuje funkcję user_lotto_numbers ().

    Sprawdza, czy funkcja poprawnie pobiera 6 unikalnych liczb od użytkownika.
    """
    user_numbers = {3, 5, 6, 7, 8, 9}
    with patch('builtins.input', side_effect=user_numbers):
        result = mf.user_lotto_numbers()

    assert isinstance(result, set)
    assert len(result) == 6


def test_lotto_numbers():
    """
    Test the lotto_numbers() function.

    Verifies if the function generates a set of 6 unique numbers within the range from 1 to 49.
    """
    numbers = mf.lotto_numbers()
    drawn_numbers = sorted(list(mf.lotto_numbers()))

    assert len(numbers) == 6
    assert isinstance(numbers, set)
    assert drawn_numbers[0] >= 1
    assert drawn_numbers[-1] <= 49


def test_compare_numbers():
    """
    Test the compare_numbers() function.

    Ensures that the function correctly returns the number of matched numbers between two sets.
    """
    set1 = {3, 4, 23, 29, 35, 44}
    set2 = {44, 15, 5, 6, 22, 23}

    matched_numbers = mf.compare_numbers(set1, set2)

    assert matched_numbers == 2


def test_how_many_numbers_matched():
    """
    Test the how_many_numbers_matched() function.

    Validates the function's ability to count the matches between
     the user's numbers and lotto numbers.
    """
    mf.user_numbers = {1, 2, 3, 4, 5, 6}
    mf.lotto_numbers = lambda: {1, 2, 3, 4, 5, 6}
    result = mf.how_many_numbers_matched()
    assert result == (1, 0, 0, 0)


def test_years_needed_to_win():
    """
    Test the years_needed_to_win() function.

    Checks the function's ability to calculate the years needed to win the lottery
     based on the number of games played.
    """
    games_case1 = 156000
    expected_result1 = (1000, 0, 0)

    games_case2 = 4000545
    expected_result2 = (25644, 27, 0)

    games_case3 = 12456432
    expected_result3 = (79848, 48, 0)

    assert mf.years_needed_to_win(games_case1) == expected_result1
    assert mf.years_needed_to_win(games_case2) == expected_result2
    assert mf.years_needed_to_win(games_case3) == expected_result3


def test_main():
    pass
