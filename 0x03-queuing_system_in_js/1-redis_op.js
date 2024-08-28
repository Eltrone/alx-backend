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

// Fonction pour définir une nouvelle école dans Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Fonction pour afficher la valeur d'une école
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(err);
    } else {
      console.log(reply);
    }
  });
}

// Appels de fonctions pour tester les opérations Redis
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
