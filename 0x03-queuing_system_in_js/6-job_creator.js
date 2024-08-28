// Importing necessary modules
import kue from 'kue';
import { createClient } from 'redis';

// Create a queue with Kue
const queue = kue.createQueue({
    redis: {
        createClientFactory: function () {
            return createClient({ url: 'redis://127.0.0.1:6379' });
        }
    }
});

// Job data object
const jobData = {
    phoneNumber: '415-123-4567',
    message: 'This is the code to verify your account'
};

// Creating a job in the 'push_notification_code' queue
const job = queue.create('push_notification_code', jobData)
    .save((err) => {
        if (err) {
            console.error('Notification job failed', err);
        } else {
            console.log(`Notification job created: ${job.id}`);
        }
    });

// Event listener for job completion
job.on('complete', () => {
    console.log('Notification job completed');
});

// Event listener for job failure
job.on('failed', (err) => {
    console.log('Notification job failed', err);
});
