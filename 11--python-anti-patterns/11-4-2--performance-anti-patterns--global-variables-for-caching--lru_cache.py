"""
Use specialized caching libraries, for example, `lru_cache`
instead of global variables for caching.
"""
import time
import random
from functools import lru_cache


def query_db(user_id):
    """ Simulates querying a database. """
    time.sleep(random.uniform(1.0, 2.0))

    user_data = {
        1: {"name": "Alice", "email": "alice@example.com"},
        2: {"name": "Bob", "email": "bob@example.com"},
        3: {"name": "Charlie", "email": "charlie@example.com"},
    }

    result = user_data.get(user_id, {"error": "User not found"})
    return result


# not recommended
_cache = {}  # global variable for caching


def get_data_v1(user_id):
    if user_id in _cache:
        result = _cache[user_id]
    else:
        result = query_db(user_id)
        _cache[user_id] = result
    return result


# better
@lru_cache(maxsize=100)
def get_data_v2(user_id):
    return query_db(user_id)


if __name__ == "__main__":
    print(get_data_v1(1))
    # {'name': 'Alice', 'email': 'alice@example.com'}
    print(get_data_v2(1))
    # {'name': 'Alice', 'email': 'alice@example.com'}
