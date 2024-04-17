from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import grpc

from grpc_server.notification_pb2 import NotificationRequest, NotificationResponse
from grpc_server.notification_pb2_grpc import NotificationServiceStub


@login_required
def send_notification(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        with grpc.insecure_channel('localhost:50051') as channel:
            # Usando o stub importado de central_notificacoes.grpc_server
            stub = NotificationServiceStub(channel)
            # Usando NotificationRequest de central_notificacoes.grpc_server
            response = stub.SendNotification(NotificationRequest(message=message))
            return JsonResponse({'confirmation': response.confirmation})
