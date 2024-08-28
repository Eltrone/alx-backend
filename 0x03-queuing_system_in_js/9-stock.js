const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

const app = express();
const port = 1245;

// Initialize Redis client
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Product data
const listProducts = [
    { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
    { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
    { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
    { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

// Helper function to find product by ID
function getItemById(id) {
    return listProducts.find(product => product.id === id);
}

// Reserve stock by item ID
async function reserveStockById(itemId, stock) {
    await setAsync(`item.${itemId}`, stock);
}

// Get current reserved stock by item ID
async function getCurrentReservedStockById(itemId) {
    const stock = await getAsync(`item.${itemId}`);
    return stock !== null ? parseInt(stock) : null;
}

// Routes
// Get list of all products
app.get('/list_products', (req, res) => {
    res.json(listProducts.map(product => ({
        itemId: product.id,
        itemName: product.name,
        price: product.price,
        initialAvailableQuantity: product.stock
    })));
});

// Get product details by ID
app.get('/list_products/:itemId', async (req, res) => {
    const item = getItemById(parseInt(req.params.itemId));
    if (!item) {
        return res.status(404).json({ status: 'Product not found' });
    }
    const currentStock = await getCurrentReservedStockById(item.id) || item.stock;
    res.json({
        itemId: item.id,
        itemName: item.name,
        price: item.price,
        initialAvailableQuantity: item.stock,
        currentQuantity: currentStock
    });
});

// Reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
    const item = getItemById(parseInt(req.params.itemId));
    if (!item) {
        return res.status(404).json({ status: 'Product not found' });
    }
    const currentStock = await getCurrentReservedStockById(item.id) || item.stock;
    if (currentStock <= 0) {
        return res.json({ status: 'Not enough stock available', itemId: item.id });
    } else {
        await reserveStockById(item.id, currentStock - 1);
        res.json({ status: 'Reservation confirmed', itemId: item.id });
    }
});

// Handle Redis connection errors
client.on('error', (err) => console.log('Redis Client Error', err));

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
