require("dotenv").config(); 

const express = require("express");
const mongoose = require("mongoose");

const app = express();

mongoose.connect(process.env.DATABASE_URL);
const db = mongoose.connection;

db.on("error", (error) => console.error(error));

db.once("open", () => console.log("Connected to Database"));

app.use(express.json());

const cors = require("cors");
app.use(cors());

const appointmentsRouter = require("./routes/appointmentRoutes");
app.use('/appointments', appointmentsRouter);

const audioRouter = require("./routes/audioRoutes");
app.use('/audio', audioRouter);

const patientsRouter = require("./routes/patientRoutes");
app.use('/patients', patientsRouter);

app.listen(3001, () => {
  console.log("Server is running on port 3001");
});
