# RateLimiterPy

A Python project that implements a **Rate Limiter** decorator to restrict function calls within a specified time window. This helps prevent excessive calls and protects system resources.

---

## Description

RateLimiterPy uses Python decorators to monitor and control how many times a function can be called within a given time frame. By storing timestamps of recent calls in a local list (closure), the decorator allows a function to run only if the number of calls in the defined period is below a specified limit. If the limit is exceeded, a `ValueError` is raised.

---

## Features

- **Function Call Control:** Limit the number of function executions per time period.
- **High-Resolution Timing:** Uses `time.perf_counter()` for precise measurement.
- **Closure-Based Storage:** Keeps call timestamps local to each decorated function.
- **Simple and Extensible:** Easy to apply to any function requiring rate limiting.

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YourUsername/RateLimiterPy.git
   cd RateLimiterPy
   ```

2. **(Optional) Create a virtual environment and install dependencies:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use: env\Scripts\activate
   pip install -r requirements.txt
   ```
   *Note: This project uses only standard libraries (e.g., `time`, `functools`), so no additional packages are required.*

---

## Usage

Apply the rate limiter decorator to your function by specifying the maximum number of allowed calls and the time window (in seconds).

### **Example:**

```python
import time
from Rate_Limiter import Rate_limiter

@Rate_limiter(3, 5)
def say_hello(name):
    return f"Hello to {name}"

if __name__ == "__main__":
    # This loop will raise a ValueError once the rate limit is exceeded
    for _ in range(10):
        try:
            print(say_hello("sara"))
        except ValueError as e:
            print(e)
    
    time.sleep(5)  # Wait for the rate limiter to reset
    print(say_hello("ali"))
```

---

## Testing

Tests are written using **pytest** to verify the behavior under various conditions including valid calls, invalid (exceeding) calls, and edge cases.

### **Run Tests:**

1. Ensure you have pytest installed:
   ```bash
   pip install pytest
   ```

2. Run the tests:
   ```bash
   pytest
   ```

### **Example Test Cases:**

- **Valid Calls:** Confirm that functions return correct values when calls are within limits.
- **Invalid Calls:** Verify that a `ValueError` is raised when the rate limit is exceeded.
- **Edge Cases:** Test boundary conditions with appropriate use of `time.sleep()` to reset the limiter.

---

## Contributing

Contributions are welcome! If you have suggestions or improvements:
- Fork the repository.
- Create a feature branch.
- Commit your changes and open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For any questions or issues, please open an issue on GitHub or contact [Your Name](mailto:your.email@example.com).

---

*RateLimiterPy helps you write more robust and resource-efficient Python applications by enforcing controlled function execution.*
```
