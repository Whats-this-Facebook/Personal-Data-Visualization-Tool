from Plots.dataQuantity import get_directory_size
from Plots.dataQuantity import bytesToString
import pytest

@pytest.fixture

def test_get_directory_size():
    assert get_directory_size("../..") > 1

def test_bytesToString_1():
    assert bytesToString(1000) == "1.0 kilobytes"

def test_bytesToString_1():
    assert bytesToString(1000000) == "1.0 megabytes"

def test_bytesToString_1():
    assert bytesToString(1000000000) == "1.0 gigabytes"
