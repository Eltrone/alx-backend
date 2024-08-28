// Importation du module redis
import redis from 'redis';

// Création d'un client Redis
const client = redis.createClient({
  url: 'redis://127.0.0.1:6379'  // Assurez-vous que l'URL est correcte
});

// Gestion de la connexion réussie
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Gestion des erreurs
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

// Fonction pour créer et stocker un hash
function createAndStoreHash() {
  const hashKey = 'HolbertonSchools';
  client.hset(hashKey, 'Portland', '50', redis.print);
  client.hset(hashKey, 'Seattle', '80', redis.print);
  client.hset(hashKey, 'New York', '20', redis.print);
  client.hset(hashKey, 'Bogota', '20', redis.print);
  client.hset(hashKey, 'Cali', '40', redis.print);
  client.hset(hashKey, 'Paris', '2', redis.print);
}

// Fonction pour afficher le hash
function displayHash() {
  const hashKey = 'HolbertonSchools';
  client.hgetall(hashKey, (err, obj) => {
    if (err) {
      console.error(err);
    } else {
      console.log(obj);
    }
  });
}

// Appel des fonctions
createAndStoreHash();
setTimeout(displayHash, 500);  // Attente pour garantir que le hash est stocké avant de le récupérer
