// Importation des modules nécessaires
import redis from 'redis';
import { promisify } from 'util';

// Création d'un client Redis
const client = redis.createClient({
  url: 'redis://127.0.0.1:6379'  // Assurez-vous que l'URL est correcte
});

// Promisify les méthodes nécessaires
const getAsync = promisify(client.get).bind(client);

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

// Fonction asynchrone pour afficher la valeur d'une école
async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(err);
  }
}

// Test des fonctions
(async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  // Attendre un court délai avant de récupérer la valeur pour s'assurer qu'elle est enregistrée
  setTimeout(async () => {
    await displaySchoolValue('HolbertonSanFrancisco');
  }, 500);
})();
