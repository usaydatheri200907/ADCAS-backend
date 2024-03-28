require("dotenv").config();
const express = require("express");
const mongoose = require("mongoose");
const connectToMongoDB = require("./mongoDB");

const app = express();

connectToMongoDB()
  .then((database) => {
    app.locals.database = database;
    console.log("Connected to MongoDB");
  })
  .catch((error) => {
    console.error("Failed to connect to MongoDB:", error);
    process.exit(1);
  });

const db = mongoose.connection;
db.on("error", (error) => console.error(error));

db.once("open", () => console.log("Connected to Database"));

app.use(express.json());

const cors = require("cors");
app.use(cors());

const appointmentsRouter = require("./routes/appointmentRoutes");
app.use("/appointments", appointmentsRouter);

const audioRouter = require("./routes/audioRoutes");
app.use("/audio", audioRouter);

const patientsRouter = require("./routes/patientRoutes");
app.use("/patients", patientsRouter);

app.listen(3001, () => {
  console.log("Server is running on port 3001");
});
