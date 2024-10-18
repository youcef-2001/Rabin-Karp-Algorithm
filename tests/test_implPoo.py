
import pytest
from implementations.implem import Hasher , Searcher
from ressources.chaines import texte1 , texte2 , texte3
pat = "hey"
hasher =None
searcher =None


def test_hasher_init():

    hasher = Hasher(texte2, 101, len(pat))
    assert (not hasher == None)



def test_Searcher_init():

    hasher = Hasher(texte2, 101, len(pat))
    assert (not hasher == None)
    hasher.calculHashes()# rempli le dictionnaire des hash
    searcher = Searcher(hasher , pat)
    assert(not searcher == None)
    assert(searcher.searchPattern() ==[15, 45, 54, 222, 240, 270, 279, 447])

def test_hash_function():
    
    hasher = Hasher(texte2, 101, len(pat))
    assert (not hasher == None)
    assert ( not hasher.calculHash("salut") ==  hasher.calculHash("lutsa"))


def test_Search():

    hasher = Hasher(texte2, 101, len(pat))
    assert (not hasher == None)
    hasher.calculHashes()# rempli le dictionnaire des hash
    searcher = Searcher(hasher , pat)
    assert(not searcher == None)
    assert(searcher.searchPattern() ==[15, 45, 54, 222, 240, 270, 279, 447])