const express = require('express');
const router = express.Router();
const Appointment = require('../models/appointment');

// Route to add a new appointment
router.post('/add', async (req, res) => {
  try {
    const { title, date, time, description } = req.body;

    const newAppointment = new Appointment({
      title,
      date,
      time,
      description,
    });

    const savedAppointment = await newAppointment.save();

    res.json(savedAppointment);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Route to get all appointments
router.get('/all', async (req, res) => {
  try {
    const allAppointments = await Appointment.find();
    res.json(allAppointments);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Route to update an appointment
router.patch('/:id', async (req, res) => {
  try {
    const appointment = await Appointment.findById(req.params.id);

    if (!appointment) {
      return res.status(404).json({ message: 'Appointment not found' });
    }

    // Update the appointment
    Object.assign(appointment, req.body);

    const updatedAppointment = await appointment.save();
    res.json(updatedAppointment);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Route to delete an appointment
router.delete('/delete/:id', async (req, res) => {
  try {
    const appointmentId = req.params.id;

    const deletedAppointment = await Appointment.findByIdAndDelete(appointmentId);

    if (!deletedAppointment) {
      return res.status(404).json({ message: 'Appointment not found' });
    }

    res.json({ message: 'Appointment deleted successfully' });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

module.exports = router;
