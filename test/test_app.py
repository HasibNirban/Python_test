from my_app.app import add, sub

def test_add():
    assert add(6,4)==10
    assert add(5,5)==10

def test_sub():
    assert sub(4,2)==2
    assert sub(6,2)==4
