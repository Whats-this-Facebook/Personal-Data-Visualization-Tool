from Plots.wordCounter import mostFreq
import pytest

@pytest.fixture
def data_set():
   return 'Welcome to the world of Geeks This portal has been created to provide well written well thought and well explained solutions for selected questions If you like Geeks for Geeks and would like to contribute here is your chance You can write article and mail your article to contribute at geeksforgeeks org See your article appearing on the Geeks for Geeks main page and help thousands of other Geeks. '

def test_empty_data_set():
    assert mostFreq("",1) == None 

def test_whitespace_data_set():
    assert mostFreq("    ",1) == None 

def test_punctuation_data_set():
    assert mostFreq(",;:.~`",1) == None 

def test_most_freq_word(data_set):
    assert mostFreq(data_set,1) == [('geeks', 6)]

def test_top_ten(data_set):
    assert mostFreq(data_set,10) == [('geeks', 6), ('well', 3), ('article', 3), ('like', 2), ('contribute', 2), ('welcome', 1), ('world', 1), ('portal', 1), ('created', 1), ('provide', 1)]

