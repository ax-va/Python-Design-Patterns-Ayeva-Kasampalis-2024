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
    See `06*/06-3*/README.md` for more details.

- Pull the official Redis image from Docker Hub:
    ```unix
    $ docker pull redis
    ...
    Status: Downloaded newer image for redis:latest
    docker.io/library/redis:latest
    ```
  
- Start the Redis server running in a Docker container:
    ```unix
    $ docker run --name myredis -p 6379:6379 redis
    ...
    1:M 12 Mar 2025 21:17:51.712 * Running mode=standalone, port=6379.
    1:M 12 Mar 2025 21:17:51.713 * Server initialized
    1:M 12 Mar 2025 21:17:51.713 * Ready to accept connections tcp
    ```
  
- Stop the Redis server running in Docker:
  ```unix
  $ docker ps
  CONTAINER ID   IMAGE     COMMAND                  CREATED        STATUS        PORTS                                         NAMES
  22ea356f239c   redis     "docker-entrypoint.s…"   21 hours ago   Up 21 hours   0.0.0.0:6379->6379/tcp, [::]:6379->6379/tcp   myredis
  $ docker stop 22ea356f239c
  22ea356f239c
  ```

- Install the Python's client for Redis, the **redis-py** package:

    - https://pypi.org/project/redis/
    - https://github.com/redis/redis-py
    - https://snyk.io/advisor/python/redis
    
    ```unix
    $ pip install redis
    ```
  
### Faker

- Faker is used for generating fake quotes that will populate the database:

  - https://pypi.org/project/Faker/
  - https://github.com/joke2k/faker
  - https://snyk.io/advisor/python/faker
  
  ```unix
  $ pip install Faker
  ```