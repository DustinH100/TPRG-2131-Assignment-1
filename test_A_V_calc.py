#TPRG 2131 test_A_V_calc.py A simplistic Area/Volume calculator pytest
#TPRG 2131 Fall 2023 Assignment 1
#Oct 15, 2023
#Dustin Horne, 100844416
# This program is strictly my own work. Any material
# beyond course learning materials that is taken from
# the Web or other sources is properly cited, giving
# credit to the original author(s).
'''
This file is to be the test_A_V_calc.py file to be used with your A_V_calc.py and pytest.
This must test each of your Area/Volume functions, with a least 3 examples for each of the
5 functions your chose to use.

As this stands it will NOT work with your A_V_calc.py file.
'''

#from assertions import add2
import pytest 
import A_V_calc_starter

def test_arec1():
    assert A_V_calc.arec(2, 2) == 4

def test_arec2():
    assert A_V_calc.arec(2, 3) == 6
    
def test_arec3():
    assert A_V_calc.arec(3, 3) == 9
    
def test_asqr1():
    assert A_V_calc.asqr(2) == 4
    
def test_asqr2():
    assert A_V_calc.asqr(3) == 9
    
def test_asqr3():
    assert A_V_calc.asqr(4) == 16
    
def test_acir1():
    assert A_V_calc.acir(2) == 12.566370614359172
    
def test_acir2():
    assert A_V_calc.acir(3) == 28.274333882308138

def test_acir3():
    assert A_V_calc.acir(4) == 50.26548245743669
    
def test_acub1():
    assert A_V_calc.acub(2) == 24
    
def test_acub2():
    assert A_V_calc.acub(3) == 54

def test_acub3():
    assert A_V_calc.acub(4) == 96
    
def test_vcub1():
    assert A_V_calc.vcub(2) == 8

def test_vcub2():
    assert A_V_calc.vcub(3) == 27

def test_vcub3():
    assert A_V_calc.vcub(4) == 64
    