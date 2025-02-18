# Architectural Desing Patterns

## Microservices

The *Microservice Architecture* pattern, or *Microservices*, is used to build
an application as a set of loosely coupled, collaborating services.
These services are loosely coupled, independently deployable, and communicate via well-defined APIs.
We usually run those services packed as containers with our application server,
dependencies and runtime libraries, compiled code, configurations, etc.

## Example: a payment service using gRPC.

- gRPC is a high-performance universal RPC framework
that uses *Protocol Buffers (protobuf)* as its interface description language:

https://pypi.org/project/grpcio/
https://snyk.io/advisor/python/grpcio

```unix
$ python -m pip install grpcio
```

- gRPC-tools

https://pypi.org/project/grpcio-tools/
https://snyk.io/advisor/python/grpcio-tools

```unix
$ python -m pip install grpcio-tools
```

- Compile the `payment.proto` file into Python code using the protobuf compiler `protoc` using the form:
```unix
$ python -m grpc_tools.protoc -I<PROTO_DIR> --python_out=<OUTPUT_DIR> --grpc_python_out=<OUTPUT_DIR> <PROTO_FILES>
```

- Install `python3-apt` and link it to your virtual environment:
```unix
$ sudo apt-get update
$ sudo apt-get install python3-apt
$ ln -s /usr/lib/python3/dist-packages/apt_pkg.cpython-*.so <path/to/venv>/lib/python3.*/site-packages/
```

- Navigate to `06*/06-2-1*` and generate `payment_pb2.py` and `payment_pb2_grpc.py` 
that are not to be manually edited.:
```
$ python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. payment.proto
```

- Provide in `payment_service.py` the service logic for the payment processing, 
extending what has been provided in the generated `.py` files. 

- Write in `client.py` a test client with code that calls the service using gRPC.

- Start the service:
```
$ python payment_service.py
Payment Processing Service ready!

```

- In another terminal, navigate to `06*/06-2-1*` and run the client:
```
$ python client.py
Payment Service responded.
Response payment ID: 12345
Response status: SUCCESS
```