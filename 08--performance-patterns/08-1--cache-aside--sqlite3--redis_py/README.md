## Performance Patterns

### Cache-Aside

When data is more frequently read than updated, applications can use a cache
to optimize repeated access to information stored in a database or data store.
In the Cache-Aside pattern, Cache-Aside, where, frequently accessed data is stored in a cache, 
reducing the need to fetch data from the data store repeatedly.

### Redis

- Check whether Docker is installed:
    ```unix
    $ docker --version
    Docker version 28.0.0, build f9ced58
    ```
    For more details, see `06*/06-3*/README.md`.

- Pull the official Redis image from Docker Hub:
    ```unix
    $ docker pull redis
    ...
    Status: Downloaded newer image for redis:latest
    docker.io/library/redis:latest
    ```
  
- Start the Redis server as a Docker container:
    ```unix
    $ docker run --name myredis -p 6379:6379 redis
    ...
    1:M 12 Mar 2025 21:17:51.712 * Running mode=standalone, port=6379.
    1:M 12 Mar 2025 21:17:51.713 * Server initialized
    1:M 12 Mar 2025 21:17:51.713 * Ready to accept connections tcp
    ```

- Install the Python's **redis-py** package:

    - https://pypi.org/project/redis/
    - https://github.com/redis/redis-py
    - https://snyk.io/advisor/python/redis
    ```unix
    $ pip install redis
    ```