import time
from functools import wraps
        
def Rate_limiter(calls , seconds):
    def decorator(func):
        timestamps = [] # For each function that impelement this Decorator 
        @wraps(func)
        def wrapper(name):
            now = time.monotonic()
            while timestamps and now - timestamps[0] > seconds:
                timestamps.pop(0)
            if len(timestamps) >= calls:
                raise ValueError("Rate limit exceeded!") 
            timestamps.append(now)
            return func(name)
        return wrapper
    return decorator

@Rate_limiter(3 , 5)
def say_hello(name):
    return f"say hello to {name}"

def main():
    for _ in range(10):
        try:
            say_hello('sara')
        except ValueError as e:
            print(e)
    
    time.sleep(5)
    print(say_hello('ali'))
    print(say_hello('reza'))

if __name__ == "__main__":
    main()