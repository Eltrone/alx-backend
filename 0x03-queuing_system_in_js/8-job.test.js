// 8-job.test.js

import chai from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

const expect = chai.expect;

describe('createPushNotificationsJobs', function() {
    let queue;

    before(() => {
        queue = kue.createQueue();
        queue.testMode.enter();
    });

    after(() => {
        queue.testMode.clear();
        queue.testMode.exit();
    });

    it('should display an error message if jobs is not an array', function() {
        expect(() => createPushNotificationsJobs({}, queue)).to.throw(Error, 'Jobs is not an array');
    });

    it('should create two new jobs to the queue', function(done) {
        const jobs = [
            { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
            { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' }
        ];

        createPushNotificationsJobs(jobs, queue);

        setTimeout(() => {
            expect(queue.testMode.jobs.length).to.equal(2);
            expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
            expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);
            expect(queue.testMode.jobs[1].data).to.eql(jobs[1]);
            done();
        }, 50); // Delay to allow async operations to complete
    });
});
