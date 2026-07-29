from function import hello

def test_default():
    assert hello() == "hello"


# create __init__.py file in the tests folder python will treat the folder as package
# package is a way to organize related Python modules into a folder.