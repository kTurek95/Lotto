"""
Module name: main_function
Description: This module contains all the functions needed to run the main module.
Author: Kacper Turek
Date: 2023-07-17
"""

import random

user_numbers = set()
COST_OF_SINGLE_DRAW = 3
allowed_numbers = range(1, 50)


def user_lotto_numbers():
    """
    A function that takes 6 numbers from the user and stores them in a variable.
     If a number is outside the range, it displays an error to the user and asks for another number.
    :return: 6 numbers from the user.
    """
    while True:
        user_number = int(input('Podaj liczbę w przedziale od 1 do 49: '))
        if user_number in range(1, 50):
            user_numbers.add(user_number)
        else:
            print('Podałeś liczbę spoza przedziału')
        if len(user_numbers) == 6:
            break

    return user_numbers


def lotto_numbers():
    """
    Function that randomly selects 6 numbers from the range of 1 to 49.
    :return: 6 pseudorandom numbers.
    """

    return set(random.sample(allowed_numbers, k=6))


def compare_numbers(set1, set2):
    """
        A function that checks how many identical numbers are in two sets.
        :param set1: First set.
        :param set2: Second set.
        :return: The number of identical numbers.
        """

    matched_numbers = set1.intersection(set2)
    return len(matched_numbers)


def how_many_numbers_matched():
    """
    The function checks how many times we hit a particular prize in the lottery.
    :return: The number of wins for individual lottery numbers.
    """

    counter = 0
    counter3 = 0
    counter4 = 0
    counter5 = 0

    while True:
        counter += 1
        lotto_nums = lotto_numbers()
        common_elements = compare_numbers(user_numbers, lotto_nums)
        if common_elements == 6:
            break
        if common_elements == 5:
            counter5 += 1
        if common_elements == 4:
            counter4 += 1
        if common_elements == 3:
            counter3 += 1

    return counter, counter5, counter4, counter3


def years_needed_to_win(games):
    """
    Calculate the number of years, weeks, and days needed to win the lottery.
    :param games: The total number of attempts (games) made to win the lottery.
    :return: number of years, weeks, and remaining days needed to win.
    """
    games_per_week = 3
    games_per_year = 52 * games_per_week

    total_years = games // games_per_year
    remaining_games = games % games_per_year

    total_weeks = remaining_games // games_per_week
    remaining_days = remaining_games % games_per_week * 7

    return total_years, total_weeks, remaining_days


def main():
    """
    The main function of the program displaying essential information.
    """
    user_lotto_numbers()
    counter_value, counter5_value, counter4_value, counter3_value = how_many_numbers_matched()
    years, weeks, days = years_needed_to_win(counter_value)
    total_cost = COST_OF_SINGLE_DRAW * 3 * counter_value
    print(f'Brawo! Zdobyłeś 6 za {counter_value} razem'
          f' natomiast 5 zdobyłeś {counter5_value} razy,'
          f' 4 zdobyłeś {counter4_value} razy,'
          f' a 3 {counter3_value} razy')
    print(f'Zajęło Ci to {years} lat, {weeks} tygodni i {days} dni.')
    print(f'Koszt inwestycji wyniósł {total_cost}')
