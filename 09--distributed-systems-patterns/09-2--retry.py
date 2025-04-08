"""
Retry

When communicating with an external component or service,
the *Retry* pattern is used to call the service again,
perhaps immediately or after some timeout (such as a few seconds),
to avoid or minimize the occurrence of transient faults or failures
that are not related to the application's logic itself.
"""
import logging
import random
import time

# Add configuration for logging
logging.basicConfig(level=logging.DEBUG)


def retry(num_attempts):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_attempts):
                try:
                    result = func(*args, **kwargs)
                except Exception as e:
                    time.sleep(1)
                    logging.debug(e)
                else:
                    return result
            return f"Failure after all {num_attempts} attempts."

        return wrapper

    return decorator


@retry(num_attempts=3)
def connect_to_database(i):
    """ Simulates a database connection. """
    if random.randint(0, 1):
        raise Exception(f"Connection #{i}: temporary database error")
    return "Connected to database"


if __name__ == "__main__":
    for i in range(1, 6):
        logging.info(f"Connection #{i}")
        print(f"--> {connect_to_database(i)}")
    # INFO:root:Connection #1
    # INFO:root:Connection #2
    # --> Connected to database
    # DEBUG:root:Connection #2: temporary database error
    # DEBUG:root:Connection #2: temporary database error
    # INFO:root:Connection #3
    # INFO:root:Connection #4
    # --> Connected to database
    # --> Connected to database
    # DEBUG:root:Connection #4: temporary database error
    # DEBUG:root:Connection #4: temporary database error
    # --> Failure after all 3 attempts.
    # --> Connected to database
    # DEBUG:root:Connection #4: temporary database error
    # INFO:root:Connection #5