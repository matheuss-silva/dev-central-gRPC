from concurrent import futures
import grpc
# Importações ajustadas para o novo caminho relativo
from .grpc_server.notification_pb2 import NotificationRequest, NotificationResponse
from .grpc_server.notification_pb2_grpc import NotificationServiceServicer, add_NotificationServiceServicer_to_server

class NotificationService(NotificationServiceServicer):
    def SendNotification(self, request, context):
        # Processa a notificação aqui
        return NotificationResponse(confirmation='Notificação recebida: ' + request.message)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Usando a função de adição do módulo correto
    add_NotificationServiceServicer_to_server(NotificationService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
