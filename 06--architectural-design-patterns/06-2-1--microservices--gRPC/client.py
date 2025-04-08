import grpc
import payment_pb2
import payment_pb2_grpc


with grpc.insecure_channel("localhost:50051") as chan:
    stub = payment_pb2_grpc.PaymentServiceStub(chan)
    resp = stub.ProcessPayment(
        payment_pb2.PaymentRequest(
            order_id="order123",
            amount=99.99,
            currency="EUR",
            user_id="user456",
        )
    )
    print("Payment Service responded.")
    print(f"Response payment ID: {resp.payment_id}")
    print(f"Response status: {resp.status}")