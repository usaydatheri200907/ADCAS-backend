const mongoose = require("mongoose");

const patientSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true
  },
  age: {
    type: Number,
    required: true
  },
  gender: {
    type: String,
    required: true
  },
  address: {
    type: String
  },
  phoneNumber: {
    type: String
  },
  email: {
    type: String
  },
  appointmentHistory: [{
    date: {
      type: Date,
      required: true
    },
    diagnosis: {
      type: String
    },
    prescription: {
      type: String
    }
  }]
});

module.exports = mongoose.model("Patient", patientSchema);
