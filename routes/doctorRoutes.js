// routes/doctorRoutes.js
const express = require('express');
const router = express.Router();
const Doctor = require('../models/doctor');

// Login route
router.post('/login', async (req, res) => {
  const { email, password } = req.body;
  const doctor = await Doctor.findOne({ email, password });
  if (doctor) {
    res.status(200).send('Login successful');
  } else {
    res.status(401).send('Invalid email or password');
  }
});

// Signup route
router.post('/signup', async (req, res) => {
    const { name, email, password, confirmPassword } = req.body;
    
    // Check if password and confirm password match
    if (password !== confirmPassword) {
      return res.status(400).send('Passwords do not match');
    }
  
    const doctor = new Doctor({ name, email, password });
    try {
      await doctor.save();
      res.status(201).send('Doctor signed up successfully');
    } catch (err) {
      res.status(400).send(err.message);
    }
  });

module.exports = router;
