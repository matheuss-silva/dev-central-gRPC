import grpc
import notification_pb2
import notification_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = notification_pb2_grpc.NotificationServiceStub(channel)
        response = stub.SendNotification(notification_pb2.NotificationRequest(message='Olá, servidor!'))
        print("Cliente recebeu: " + response.confirmation)

if __name__ == '__main__':
    run()
