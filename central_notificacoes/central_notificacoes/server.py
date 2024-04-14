from concurrent import futures
import grpc
import notification_pb2
import notification_pb2_grpc
from .grpc_server.notification_pb2 import NotificationRequest, NotificationResponse
from .grpc_server.notification_pb2_grpc import NotificationServiceStub

class NotificationService(notification_pb2_grpc.NotificationServiceServicer):
    def SendNotification(self, request, context):
        # Processa a notificação aqui
        return notification_pb2.NotificationResponse(confirmation='Notificação recebida: ' + request.message)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    notification_pb2_grpc.add_NotificationServiceServicer_to_server(NotificationService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
