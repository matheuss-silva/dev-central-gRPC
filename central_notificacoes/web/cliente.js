// Import the generated stubs for the Notification service
import { NotificationServicePromiseClient } from './notification_pb_service';
import { NotificationRequest } from './notification_pb';

const client = new NotificationServicePromiseClient('http://localhost:8080', null, null);

function receiveNotification() {
    const request = new NotificationRequest();
    request.setMessage('Ping from the web!');

    client.sendNotification(request, {}).then(response => {
        document.getElementById('notifications').innerText = 'Received: ' + response.getConfirmation();
    }).catch(error => {
        console.error('Error receiving notification:', error);
    });
}

setInterval(receiveNotification, 5000);
