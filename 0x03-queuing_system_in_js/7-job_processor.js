// Importing necessary modules
import kue from 'kue';

// Create a queue with Kue
const queue = kue.createQueue();

// Blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notification
function sendNotification(phoneNumber, message, job, done) {
    // Track the initial job progress
    job.progress(0, 100);

    // Check if the phone number is blacklisted
    if (blacklistedNumbers.includes(phoneNumber)) {
        return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }

    // Simulate notification sending process
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    // Simulate a delay to complete the job
    setTimeout(() => {
        job.progress(100, 100);
        done();
    }, 500); // Delay of 500 ms
}

// Process the queue
queue.process('push_notification_code_2', 2, (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message, job, done);
});
