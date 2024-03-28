const mongoose = require('mongoose');

const audioSchema = new mongoose.Schema({
  filename: String,
  transcript: String,

});

const Audio = mongoose.model('Audio', audioSchema);

module.exports = Audio;
