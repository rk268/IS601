import pytest
from MyCalcc import  MyCalc
object = MyCalc()



def test_add():
    data_add = [{
        "a": 3,
        "b": 6,
        "answer": 9.0
    },
    {
        "a": -3,
        "b": -4,
        "answer": -7.0
    },
    {
        "a": 2.12345,
        "b": 1.234,
        "answer": 3.35745
    }]
    for i in data_add:
        assert object.addition(i["a"], i["b"]) == (i["answer"])


def test_add_ans():
    data_add = [
    {
        "a": "ans",
        "b": 4,
        "answer": 6.3
    },
    {
        "a": "ans",
        "b": 4,
        "answer": 10.3
    }]
    object.ans = 2.3
    for i in data_add:
        assert object.addition(i["a"], i["b"]) == (i["answer"])

def test_sub(): 
    data_sub = [{
        "a": 2,
        "b": 2,
        "answer": 0.0
    },
    {
        "a": -3,
        "b": -4,
        "answer": 1.0
    },
    {
        "a": 2.145,
        "b": 1.24,
        "answer": 0.905
    }]
    for i in data_sub:
        assert object.subtraction(i["a"], i["b"]) == (i["answer"])

def test_sub_ans():
    data_sub_ans = [
    {
        "a": float("ans"),
        "b": 4,
        "answer": -0.7000000000000002
    },
    {
        "a": float("ans"),
        "b": 4,
        "answer": -4.7
    }]
    object.ans = 3.3
    for i in data_sub_ans:
        assert object.subtraction(i["a"], i["b"]) == (i["answer"])


def test_mul(): 
    data_mul = [{
        "a": 3,
        "b": 2,
        "answer": 6.0
    },
    {
        "a": -3,
        "b": -4,
        "answer": 12.0
    },
    {
        "a": 2.3445,
        "b": 1.123,
        "answer": 2.6328735
    },]
    for i in data_mul:
        assert object.multiplication(i["a"], i["b"]) == (i["answer"])

def test_mul_ans():
    data_mul_ans = [
    {
        "a": "ans",
        "b": 4,
        "answer": 16.0
    },
    {
        "a": "ans",
        "b": -1,
        "answer": -16
    }]
    object.ans = 4
    for i in data_mul_ans:
        assert object.multiplication(i["a"], i["b"]) == (i["answer"])




def test_div(): 
    data_div = [{
        "a": 6,
        "b": 6,
        "answer": 1.0
    },
    {
        "a": -3,
        "b": -4,
        "answer": 0.75
    },
    {
        "a": 2.145,
        "b": 1.4,
        "answer": 1.5321428571428573
    },
    {
        "a": 2,
        "b": 0,
        "answer": "Error: Division by zero not defined"
    }]
    for d in data_div:
        assert object.division(d["a"], d["b"]) == (d["answer"])



def test_div_ans():
    data_div_ans = [
    {
        "a": "ans",
        "b": 2,
        "answer": 1.0
    },
    {
        "a": "ans",
        "b": 4,
        "answer": 0.25
    }]
    object.ans = 2
    for i in data_div_ans:
        assert object.division(i["a"], i["b"]) == (i["answer"])
