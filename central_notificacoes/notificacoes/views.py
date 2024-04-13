from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import grpc
import notification_pb2
import notification_pb2_grpc

@login_required
def send_notification(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = notification_pb2_grpc.NotificationServiceStub(channel)
            response = stub.SendNotification(notification_pb2.NotificationRequest(message=message))
            return JsonResponse({'confirmation': response.confirmation})
