import pytest
from Question1 import Solution

@pytest.fixture
def object():
    obj=Solution(3,3)
    return obj

    
def test_empty_list():
    board=[]
    emptyObject=Solution(0,0)
    with pytest.raises(Exception):
        emptyObject.validateInput(board)
    
def test_allXsInput(object):
    board=[['X','X','X'],['X','X','X'],['X','X','X']]
    object.validateInput(board)
    object.flipBoard(board)
    assert board==[['X','X','X'],['X','X','X'],['X','X','X']]

def test_allOsInput(object):
    board=[['O','O','O'],['O','O','O'],['O','O','O']]
    object.validateInput(board)
    object.flipBoard(board)
    assert board==[['O','O','O'],['O','O','O'],['O','O','O']]   


def test_normalInput(object):
    board=[['O','X','X'],['X','O','X'],['X','X','X']]
    object.validateInput(board)
    object.flipBoard(board)
    assert board==[['O','X','X'],['X','X','X'],['X','X','X']]


def test_InvalidInput(object):
    board=[['O','*','X'],['X','O','X'],['X','*','X']]
    with pytest.raises(Exception):
        object.validateInput(board)