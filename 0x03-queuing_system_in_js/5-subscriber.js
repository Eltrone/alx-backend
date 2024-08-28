// Importing the redis client
import redis from 'redis';

// Creating a subscriber client
const subscriber = redis.createClient({
    url: 'redis://127.0.0.1:6379'
});

// Handling connection events
subscriber.on('connect', () => {
    console.log('Redis client connected to the server');
});

subscriber.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err.message}`);
});

// Subscribing to the channel
subscriber.subscribe('holberton school channel');

// Handling messages on the channel
subscriber.on('message', (channel, message) => {
    console.log(message);
    if (message === 'KILL_SERVER') {
        subscriber.unsubscribe();
        subscriber.quit();
    }
});
