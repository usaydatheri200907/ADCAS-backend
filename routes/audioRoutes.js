const express = require('express');
const multer = require('multer');
const Audio = require('../models/audio');
const axios = require('axios');
const FormData = require('form-data');
const fs = require('fs');

const router = express.Router();
const upload = multer({ dest: 'uploads/' });

router.post('/upload', upload.single('audio'), async (req, res) => {
  try {
    const formData = new FormData();
    formData.append('audio', fs.createReadStream(req.file.path));

    const response = await axios.post('http://flask-server:5001/convert', formData, {
      headers: {
        ...formData.getHeaders(),
      },
    });

    const transcript = response.data.transcript;
    
    const newAudio = new Audio({
      filename: req.file.originalname,
      transcript: transcript
    });
    await newAudio.save();

    res.json({ transcript: transcript });
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({ error: 'Failed to process audio file' });
  }
});

module.exports = router;
