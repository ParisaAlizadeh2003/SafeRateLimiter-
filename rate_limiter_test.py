import time
import pytest
from Rate_Limiter import Rate_limiter

def main():
    test_valids()
    test_invalids()
    test_edge_values()
    
def test_valids():
  assert say_goodbye('sara') == "Goodbye to sara"
  time.sleep(3)
  assert say_goodbye('ashkan') == "Goodbye to ashkan"
  assert say_hello('sara') == "Hello to sara"
  
def test_invalids():
    with pytest.raises(ValueError, match="Rate limit exceeded!"):
       for _ in range(10):
           say_hello('sara')
    
    with pytest.raises(ValueError, match="Rate limit exceeded!"):
        for _ in range(10):
            say_goodbye('sara')

def test_edge_values():
    with pytest.raises(ValueError, match="Rate limit exceeded!"):
        for _ in range(5):
            say_hello('sara')
                 
    with pytest.raises(ValueError, match="Rate limit exceeded!"):
        for _ in range(6):
            say_hello('sara')
    time.sleep(3)
    assert say_hello('ashkan') == "Hello to ashkan"
    
    with pytest.raises(ValueError, match="Rate limit exceeded!"):
        for _ in range(2):
            say_goodbye('sara')
    time.sleep(5)
    assert say_goodbye('ashkan') == "Goodbye to ashkan"
    
    with pytest.raises(ValueError, match="Rate limit exceeded!"):
        for _ in range(3):
            say_goodbye('sara')
    time.sleep(5) 
    assert say_goodbye('ashkan') == "Goodbye to ashkan"

@Rate_limiter(2 , 5)
def say_goodbye(name):
    return f"Goodbye to {name}"

@Rate_limiter(5 , 3)
def say_hello(name):
    return f"Hello to {name}"

if __name__ == "__main__":
    main()