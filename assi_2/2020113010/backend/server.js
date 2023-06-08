const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const cors = require('cors');
const mongoose = require('mongoose');
const PORT = 4000;
const DB_NAME = "test"

// routes
// var testAPIRouter = require("./routes/testAPI");
var UserRouter = require("./routes/Users");
var VendorRouter = require("./routes/Vendors");
var ItemRouter = require("./routes/Items");
var UserAuth = require("./routes/user_auth");
var VendorAuth = require("./routes/vendor_auth");
var OrderRouter = require("./routes/Orders");
var testAPI = require("./routes/testAPI");

app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Connection to MongoDB
// mongoose.connect('mongodb://127.0.0.1:27017/' + DB_NAME, );

mongoose.connect("mongodb+srv://user:user@cluster0.zdpnr.mongodb.net/test?retryWrites=true&w=majority", {
    useNewUrlParser: true,
    useUnifiedTopology: true
} );
const connection = mongoose.connection;
connection.on("error", console.error.bind(console, "connection error: "));
connection.once('open', function () {
    console.log("MongoDB database connection established successfully !");
})

const port = process.env.PORT || 4000;

// setup API endpoints
// app.use("/testAPI", testAPIRouter);
app.use("/user", UserRouter);
app.use("/vendor", VendorRouter);
app.use("/item", ItemRouter);
app.use("/user_auth", UserAuth);
app.use("/vendor_auth", VendorAuth);
app.use("/order", OrderRouter);
app.use("/testAPI", testAPI);

app.listen(port, () => console.log(`Server is running on Port: ${port}`));
