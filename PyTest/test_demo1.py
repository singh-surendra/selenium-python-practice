import pytest

def test_m1():
    a = 3
    b = 4
    assert a+1 == b, "test failed"
    assert a == b, "test failed as a is not equal to b"

def test_m2():
    name = "selenuim"
    assert name.upper() == "SELENUIM"

def test_m3():
    assert True

def test_m4():
    assert False

def test_m5():
    assert 100 == 100

def test_m6():
    assert "suri" == "SURI"

def test_login_FB():
    assert "admin" == "admin123"

