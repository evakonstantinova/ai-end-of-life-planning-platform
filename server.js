const express = require('express');
const bodyParser = require('body-parser');
const bcrypt = require('bcrypt');
const { Pool } = require('pg');

const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

const pool = new Pool({
    user: '',       
    host: 'localhost',          
    database: 'actual_database',   
    password: 'actual_password',
    port: 5432,              
  });

// Register Route
app.post('/register', async (req, res) => {
  const { firstName, lastName, email, password } = req.body;
  const hashed = await bcrypt.hash(password, 10);
  try {
    await pool.query(
      'INSERT INTO users (first_name, last_name, email, password) VALUES ($1, $2, $3, $4)',
      [firstName, lastName, email, hashed]
    );
    res.send('Registration successful');
  } catch (err) {
    res.status(400).send('Email already exists or error occurred');
  }
});

// Login Route
app.post('/login', async (req, res) => {
  const { email, password } = req.body;
  const result = await pool.query('SELECT * FROM users WHERE email=$1', [email]);
  if (result.rows.length > 0) {
    const match = await bcrypt.compare(password, result.rows[0].password);
    if (match) {
      res.send('Login successful');
    } else {
      res.status(401).send('Invalid credentials');
    }
  } else {
    res.status(404).send('User not found');
  }
});

app.listen(3000, () => console.log('Server running on port 3000'));
