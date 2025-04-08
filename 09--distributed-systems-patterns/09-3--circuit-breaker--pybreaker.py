"""
Circuit Breaker

In the *Circuit Breaker* pattern, an integration point with an external service
is wrapped in a special (*circuit breaker*) object, which monitors for failures.
Once the failures reach a certain threshold, the circuit breaker transits to
the "open" state, immediately returning an error and preventing further calls
to the protected function.

See also:
- PyBreaker
    - https://pypi.org/project/pybreaker/
    - https://github.com/danielfm/pybreaker
    - https://snyk.io/advisor/python/pybreaker
    ```
    $ pip install pybreaker
    ```
"""
import random
import pybreaker
from datetime import datetime
from time import sleep

# 1. `fail_max` sets the maximum number of consecutive failures allowed before the circuit breaker transitions
# to the "open" state, preventing further calls to the protected function.
# 2. `reset_timeout` defines the duration (in seconds) the circuit breaker remains in the "open" state
# before transitioning to the "half-open" state,
# allowing a trial call to check if the underlying issue has been resolved.
breaker = pybreaker.CircuitBreaker(fail_max=2, reset_timeout=5)


@breaker
def fragile_function():
    if not random.choice([True, False]):
        print(" / OK", end="")
    else:
        print(" / FAIL", end="")
        raise Exception("message")


def main():
    while True:
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), end="")
        try:
            fragile_function()
        except Exception as e:
            print(f" / {type(e)}: {e}", end="")
        finally:
            print("")
            sleep(1)


if __name__ == "__main__":
    main()
    # 2025-03-19 19:34:47 / FAIL / <class 'Exception'>: message
    # 2025-03-19 19:34:48 / OK
    # 2025-03-19 19:34:49 / FAIL / <class 'Exception'>: message
    # 2025-03-19 19:34:50 / FAIL / <class 'pybreaker.CircuitBreakerError'>: Failures threshold reached, circuit breaker opened
    # 2025-03-19 19:34:51 / <class 'pybreaker.CircuitBreakerError'>: Timeout not elapsed yet, circuit breaker still open
    # 2025-03-19 19:34:52 / <class 'pybreaker.CircuitBreakerError'>: Timeout not elapsed yet, circuit breaker still open
    # 2025-03-19 19:34:53 / <class 'pybreaker.CircuitBreakerError'>: Timeout not elapsed yet, circuit breaker still open
    # 2025-03-19 19:34:54 / <class 'pybreaker.CircuitBreakerError'>: Timeout not elapsed yet, circuit breaker still open
    # 2025-03-19 19:34:55 / FAIL / <class 'pybreaker.CircuitBreakerError'>: Trial call failed, circuit breaker opened
    # 2025-03-19 19:34:56 / <class 'pybreaker.CircuitBreakerError'>: Timeout not elapsed yet, circuit breaker still open
    # 2025-03-19 19:34:57 / <class 'pybreaker.CircuitBreakerError'>: Timeout not elapsed yet, circuit breaker still open
    # 2025-03-19 19:34:58 / <class 'pybreaker.CircuitBreakerError'>: Timeout not elapsed yet, circuit breaker still open
    # 2025-03-19 19:34:59 / <class 'pybreaker.CircuitBreakerError'>: Timeout not elapsed yet, circuit breaker still open
    # 2025-03-19 19:35:00 / FAIL / <class 'pybreaker.CircuitBreakerError'>: Trial call failed, circuit breaker opened
    # 2025-03-19 19:35:01 / <class 'pybreaker.CircuitBreakerError'>: Timeout not elapsed yet, circuit breaker still open
    # 2025-03-19 19:35:02 / <class 'pybreaker.CircuitBreakerError'>: Timeout not elapsed yet, circuit breaker still open
    # 2025-03-19 19:35:03 / <class 'pybreaker.CircuitBreakerError'>: Timeout not elapsed yet, circuit breaker still open
    # 2025-03-19 19:35:04 / <class 'pybreaker.CircuitBreakerError'>: Timeout not elapsed yet, circuit breaker still open
    # 2025-03-19 19:35:05 / FAIL / <class 'pybreaker.CircuitBreakerError'>: Trial call failed, circuit breaker opened
    # 2025-03-19 19:35:06 / <class 'pybreaker.CircuitBreakerError'>: Timeout not elapsed yet, circuit breaker still open
    # 2025-03-19 19:35:07 / <class 'pybreaker.CircuitBreakerError'>: Timeout not elapsed yet, circuit breaker still open
    # 2025-03-19 19:35:08 / <class 'pybreaker.CircuitBreakerError'>: Timeout not elapsed yet, circuit breaker still open
    # 2025-03-19 19:35:09 / <class 'pybreaker.CircuitBreakerError'>: Timeout not elapsed yet, circuit breaker still open
    # 2025-03-19 19:35:10 / OK
    # 2025-03-19 19:35:11 / FAIL / <class 'Exception'>: message
    # 2025-03-19 19:35:12 / OK
    # 2025-03-19 19:35:13 / FAIL / <class 'Exception'>: message
    # 2025-03-19 19:35:14 / FAIL / <class 'pybreaker.CircuitBreakerError'>: Failures threshold reached, circuit breaker opened
    # 2025-03-19 19:35:15 / <class 'pybreaker.CircuitBreakerError'>: Timeout not elapsed yet, circuit breaker still open
    # 2025-03-19 19:35:16 / <class 'pybreaker.CircuitBreakerError'>: Timeout not elapsed yet, circuit breaker still open
    # 2025-03-19 19:35:17 / <class 'pybreaker.CircuitBreakerError'>: Timeout not elapsed yet, circuit breaker still open
    # 2025-03-19 19:35:18 / <class 'pybreaker.CircuitBreakerError'>: Timeout not elapsed yet, circuit breaker still open
    # ...
