def add(a,b):
  return a+b
  test_app.py
  from app import add
  def test_add():
    assert add(2,3)==5
