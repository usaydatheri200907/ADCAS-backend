
require("dotenv").config(); 

const express = require("express");

const app = express();

const mongoose = require("mongoose");

mongoose.connect(process.env.DATABASE_URL);
const db = mongoose.connection;

db.on("error", (error) => console.error(error));

db.once("open", () => console.log("Connected to Database"));

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send("Something broke!");
});

const cors = require("cors");
app.use(cors());

app.listen(3000, () => {
  console.log("Server is running on port 3000");
});
