import pytest
from TicTacToe import evaluate, move

#1. Evaluate Function - create at least 5 different tests for behavior of the function

#1.a The following tests when "x" wins
def test_x_wins():
    assert evaluate("oo---------------xxx") == "x wins!"


#1.b The following tests when "o" wins
def test_o_wins():
    assert evaluate("xx---------------ooo") == "o wins!"

#1.c The following tests when there is a draw
def test_draw():
    assert evaluate("xoxoxoxoxoxoxoxoxox") == "! draw"  

#1.e Tests for ongoing game
def test_ongoing_game():
    assert evaluate("xoxox---xoxoxoxoxox") == "-"

#1.e Tests when the game is still ongoing
def test_no_results():
    assert evaluate("xx---------------xoo") == "-"

# after testing the results for all 5 tests passed

#2. Move function - create at least 2 different tests

#2.a Test whether the position is taken
def test_taken_position():
    result = move("xx---------------xoo", "o", 1)
    assert result == "xx---------------xoo"

#2.b Test whether the position is available
def test_available():
    result = move("xx---------------xoo", "o", 5)
    assert result == "xx---o-----------xoo"

# after testing the results for both tests passed
    
# 3) By your own words - (as comments at the end of the created Python test file) describe:
    
# 3.a) What is a Python module and how does it differ from a Python package?
# A Python Module is a file where it has different functions or variables and their own meaning and the use of them.
# While a package is a collection of modules.
    
# 3.b) What are side effects and give some examples.
# When a module is used in a program, a side effects happen with noticeables changes and actions.
# An example would be in case you have a module called "addition" where you set the result to sum up two numbers and you try to use it in another script.
# The result can be different when using it in the other script and in this case effects the state of the module.
    
# 3.c) What are Exceptions and what to do if third-party code that we use throws them?
# Exceptions occur when executing the program and unexpected events happen which can then mess up the whole execution.
# The issues can be approached slowly. In these cases error messages can tell us exactly what the issue can be and lead us to solving the problem.

# 3.d) Using which keywords can you create, throw and catch your new custom Exception?
# you would be able to do it with raise, try, except, else, finally
    
# 3.e) Give examples of some benefits of testing?
# When doing testing early on it helps to detect any bugs which can be fixed. In case it's not fixed in the beginning it can be very costly and time-consuming.
# It also improves the quality of your code. When you do testing, you have results that can back up your code.
# Tests also allow you to proceed further with your changes and in implementing them.


