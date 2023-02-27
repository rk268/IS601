import pytest
from MyCalc import MyCalc
object = MyCalc()
#rk268 26 February 2023

def test_subtraction():
    assert object.subtraction(8, 3) == 5
    assert object.subtraction(3, 15) == -12
    assert object.subtraction(-9.8, 5.65) == -15.450000000000001
# Here, I have imported the pytest for running the test cases and checking if they all pass or not. Also imported 
# Mycalc as we have to test the code written there. That is why calling the subtraction function with the object is possible
# Here, I created a new test_subtraction function and will be checking the subtraction of the values given in () give the value
# written after == as a output. It it gives, then the test case is passed else it fails. 
# Here I have used assert, which return true if the condition satisfies else return false. In our case it should return 
# true always.
#rk268 26 February 2023

def test_addition():
    assert object.addition(8, 2) == 10
    assert object.addition(19.55, 98.45) == 118
    assert object.addition(-2, -3) == -5
# Here, I have imported the pytest for running the test cases and checking if they all pass or not. Also imported 
# Mycalc as we have to test the code written there. That is why calling the addition function with the object is possible
# Here, I created a new test_addition function and will be checking the addition of the values given in () give the value
# written after == as a output. It it gives, then the test case is passed else it fails. 
# Here I have used assert, which return true if the condition satisfies else return false. In our case it should return 
# true always.
#rk268 26 February 2023

def test_division():
    assert object.division(18, 3) == 6
    assert object.division(16, -2) == -8
    assert object.division(-22, -11) == 2
# Here, I have imported the pytest for running the test cases and checking if they all pass or not. Also imported 
# Mycalc as we have to test the code written there. That is why calling the division function with the object is possible
# Here, I created a new test_division function and will be checking the division of the values given in () give the value
# written after == as a output. It it gives, then the test case is passed else it fails. 
# Here I have used assert, which return true if the condition satisfies else return false. In our case it should return 
# true always.
#rk268 26 February 2023

def test_multiplication():
    assert object.multiplication(7, 5) == 35
    assert object.multiplication(8, -5) == -40
    assert object.multiplication(-2.2, -8.7) == 19.14
# Here, I have imported the pytest for running the test cases and checking if they all pass or not. Also imported 
# Mycalc as we have to test the code written there.That is why calling the multiplication function with the object is possible
# Here, I created a new test_multiplication function and will be checking the multiplication of the values given in () give 
# the value written after == as a output. It it gives, then the test case is passed else it fails. 
# Here I have used assert, which return true if the condition satisfies else return false. In our case it should return 
# true always.
#rk268 26 February 2023

def test_division_by_zero():
    # with pytest.raises(ZeroDivisionError):
    assert object.division(455, 0) == None
# Here, if the input number is divided by input number 0, then the exception is handled.
#rk268 26 February 2023

def test_addition_to_ans():
    ans= 2
    assert object.addition(ans, 3) == 5
    assert object.addition(ans, -2) == 0
    assert object.addition(ans, 5.5) == 7.5
# Here, ans is set to 2 and checked the addition of the entered input number with the ans(as input too) which was the final answer
# of the previous expression yields the expected final answer. 
# The name of the function created here is test_addition_to_ans.  
#rk268 26 February 2023

def test_subtraction_from_ans():
    ans= 18
    assert object.subtraction(ans, 8) == 10
    assert object.subtraction(ans, -2) == 20
    assert object.subtraction(ans, 19) == -1
# Here, ans is set to 18 and checked the subtraction of the entered input number with the ans(as input too) 
# which was the final answer
# of the previous expression yields the expected final answer. 
# The name of the function created here is test_subtraction_from_ans.
#rk268 26 February 2023

def test_multiplication_to_ans():
    ans= 22
    assert object.multiplication(ans, 3) == 66
    assert object.multiplication(ans, -8) == -176
    assert object.multiplication(ans, 0) == 0
# Here, ans is set to 22 and checked the multiplication of the entered input number with the ans(as input too) 
# which was the final answer
# of the previous expression yields the expected final answer. 
# The name of the function created here is test_multiplication_to_ans.
#rk268 26 February 2023

def test_division_ans():
    ans= 42
    assert object.division(ans, 7) == 6
    assert object.division(ans, -21) == -2
    assert object.division(ans, 28) == 1.5
# Here, ans is set to 42 and checked the division of the entered input number with the ans(as input too) 
# which was the final answer
# of the previous expression yields the expected final answer. 
# The name of the function created here is test_division_ans.
#rk268 26 February 2023

def test_division_ans_by_zero():
    ans= 876
    assert object.division(ans, 0) == None
#Here, ans is set to 876 and checked the division by 0 of the entered input ans(which is set to 876)
# yields the expected final answer which is error handled and None printed.
# The name of the function created here is test_division_ans_by_zero
#rk268 26 February 2023