import pytest
from CLI.readFolder import comments_str

def test_empty():
  assert comments_str([]) == ""

def test_invalid_data_1():
  assert comments_str([{'timestamp':1601406498}]) == ""

def test_invalid_data_2():
  assert comments_str([{'timestamp':1601406498, 'data':[{'comment':{'comment':"Hello"}}]}]) == " Hello"
