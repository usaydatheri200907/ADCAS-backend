require("dotenv").config();
const express = require("express");
const mongoose = require("mongoose");

const app = express();

// // MongoDB connection URI
// const MONGODB_URI = "mongodb+srv://usaydatheri200907:M0ng0d8@atlascluster.wjijzpn.mongodb.net/?retryWrites=true&w=majority";


// mongoose.connect(MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true })
//   .then(() => {
//     console.log("Connected to MongoDB");
//   })
//   .catch((error) => {
//     console.error("Failed to connect to MongoDB:", error);
//     process.exit(1);
//   });

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

const doctorRoutes = require('./routes/doctorRoutes');
const assistantRoutes = require('./routes/assistantRoutes');

app.use('/doctor', doctorRoutes);
app.use('/assistant', assistantRoutes);

app.listen(3001, () => {
  console.log("Server is running on port 3001");
});



const DB = "mongodb+srv://AutoCavity:AutoCavity@autocavity.bj6bp04.mongodb.net/"
mongoose.connect(DB,{
    useNewUrlParser:true,
    useUnifiedTopology:true
}).then(()=> console.log("Database connected"))
.catch((error)=> console.log(error.message));
