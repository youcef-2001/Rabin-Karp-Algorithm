import pytest
from implementations.implem1 import search
pat = "hey"
txt = """hey alors comment tu va salim , hey salim yeh cava ? 13 jours que je te cherche hoy""" 


def test_search():
    
    
    assert(search("hey", txt, 101 ) == [0,32])


