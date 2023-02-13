import pytest
from flipBoard import Solution

@pytest.fixture
def object():
    obj=Solution(3,3)
    return obj

    
def test_empty_list():
    board=[]
    emptyObject=Solution(0,0)
    # when we get an empty board we should raise an exception
    with pytest.raises(Exception):
        emptyObject.validateInput(board)
    
def test_allXsInput(object):
    # if all the values are X
    board=[['X','X','X'],['X','X','X'],['X','X','X']]
    object.validateInput(board)
    object.flipBoard(board)
    # The ans should remain the same
    assert board==[['X','X','X'],['X','X','X'],['X','X','X']]

def test_allOsInput(object):
    # if all the values are O
    board=[['O','O','O'],['O','O','O'],['O','O','O']]
    object.validateInput(board)
    object.flipBoard(board)
    # The ans should remain the same
    assert board==[['O','O','O'],['O','O','O'],['O','O','O']]   


def test_normalInput(object):
    board=[['O','X','X'],['X','O','X'],['X','X','X']]
    object.validateInput(board)
    object.flipBoard(board)
    assert board==[['O','X','X'],['X','X','X'],['X','X','X']]


def test_InvalidInput(object):
    # when we get a board with wrong values we should raise an exception
    board=[['O','*','X'],['X','O','X'],['X','*','X']]
    with pytest.raises(Exception):
        object.validateInput(board)
        
def test_WrongAmountInput(object):
    # when we get a board with wrong amount of column we should raise an exception
    board=[['O','*','X'],['XXX'],['X','*','X']]
    with pytest.raises(Exception):
        object.validateInput(board)