from fastapi import FastAPI
import grpc
import notification_pb2
import notification_pb2_grpc

app = FastAPI()

@app.post("/send-notification/")
def send_notification(message: str):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = notification_pb2_grpc.NotificationServiceStub(channel)
        response = stub.SendNotification(notification_pb2.NotificationRequest(message=message))
        return {"confirmation": response.confirmation}
