from wordCounter import mostFreq
import pytest

@pytest.fixture
def data_set():
   return 'Welcome to the world of Geeks This portal has been created to provide well written well thought and well explained solutions for selected questions If you like Geeks for Geeks and would like to contribute here is your chance You can write article and mail your article to contribute at geeksforgeeks org See your article appearing on the Geeks for Geeks main page and help thousands of other Geeks. '

def test_empty_data_set():
    assert mostFreq("",1) == None 

def test_whitespace_data_set():
    assert mostFreq("    ",1) == None 

def test_most_freq_word(data_set):
    assert mostFreq(data_set,1) == [('Geeks', 5)]

def test_top_ten(data_set):
    assert mostFreq(data_set,10) == [('Geeks', 5), ('to', 4), ('and', 4), ('well', 3), ('for', 3), ('your', 3), ('article', 3), ('the', 2), ('of', 2), ('like', 2)]

