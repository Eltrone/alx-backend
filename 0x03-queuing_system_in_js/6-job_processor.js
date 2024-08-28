// Importing necessary modules
import kue from 'kue';
import { createClient } from 'redis'; // Correction: import createClient

// Create a queue with Kue
const queue = kue.createQueue({
    redis: {
        createClientFactory: function () {
            return createClient({ url: 'redis://127.0.0.1:6379' });
        }
    }
});

// Function to send a notification
function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Queue process setup
queue.process('push_notification_code', (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message);
    done();
});
