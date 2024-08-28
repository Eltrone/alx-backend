// Utilisation de l'importation ES6
import redis from 'redis';

// Création d'un client Redis
const client = redis.createClient({
  url: 'redis://127.0.0.1:6379'  // Assurez-vous que l'URL correspond à votre configuration Redis
});

// Gestionnaire d'événements pour une connexion réussie
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Gestionnaire d'événements pour les erreurs de connexion
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});
