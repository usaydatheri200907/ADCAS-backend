const express = require("express");
const router = express.Router();
const Patient = require("../models/patient");

// Create a patient
router.post("/", async (req, res) => {
  try {
    const patient = new Patient({
      name: req.body.name,
      age: req.body.age,
      gender: req.body.gender
    });
    const newPatient = await patient.save();
    res.status(201).json(newPatient);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

// Read all patients
router.get("/", async (req, res) => {
  try {
    const patients = await Patient.find();
    res.json(patients);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// Update a patient
router.patch("/:id", getPatient, async (req, res) => {
  if (req.body.name != null) {
    res.patient.name = req.body.name;
  }
  if (req.body.age != null) {
    res.patient.age = req.body.age;
  }
  if (req.body.gender != null) {
    res.patient.gender = req.body.gender;
  }
  try {
    const updatedPatient = await res.patient.save();
    res.json(updatedPatient);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

// Delete a patient
router.delete("/:id", getPatient, async (req, res) => {
  try {
    await res.patient.remove();
    res.json({ message: "Deleted Patient" });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

async function getPatient(req, res, next) {
  let patient;
  try {
    patient = await Patient.findById(req.params.id);
    if (patient == null) {
      return res.status(404).json({ message: "Cannot find patient" });
    }
  } catch (err) {
    return res.status(500).json({ message: err.message });
  }

  res.patient = patient;
  next();
}

module.exports = router;
