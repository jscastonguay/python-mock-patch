from toto import Toto
from unittest.mock import MagicMock, Mock, patch
from device import Device
import toto

'''
Références:
- https://docs.python.org/3/library/unittest.mock.html
- https://docs.python.org/3/library/unittest.mock-examples.html
- https://myadventuresincoding.wordpress.com/2011/02/26/python-python-mock-cheat-sheet/
'''


# On joue avec l'objet 'Mock'
t = Toto()
#t.getNumber = MagicMock(return_value=3)
t.getNumber = Mock(return_value=3)

# Code production
print(t.getNumber(6, key = 'toto'))

t.getNumber.assert_called_with(6, key = 'toto')


# On mock la méthode 'do'  
@patch("device.Device.do")
def test_operation1(do):    
    do.return_value = 3
    t = Toto()
    r = t.operation(39)
    assert(r == 3)
    do.assert_called_once_with(2 * 39)


# Même chose que 'test_operation1' mais en utilisant la méthode par 'contexte'
def test_operation2():
    with patch("device.Device.do") as do:
        do.return_value = 3
        t = Toto()
        r = t.operation(39)
        assert(r == 3)
        do.assert_called_once_with(2 * 39)
        

# On mock le import de Device qui est fait dans le fichier 'toto'
@patch("toto.Device")
def test_operation3(mock_device : Mock):
    
    # Puisque 'mock_device' mock un objet, 'return_value' retourne l'objet qu'il mock
    # Voir https://docs.python.org/3/library/unittest.mock-examples.html#mocking-classes
    d = mock_device.return_value
    d.param = 11
    d.do.return_value = 4
    t = Toto()
    r = t.operation(39)
    assert(r == 44)
    d.do.assert_called_once_with(2 * 39)
