// to use mongoDB
const mongoose = require("mongoose");
mongoose.connect("mongodb://localhost/ece413513MongoDB", { useNewUrlParser: true, useUnifiedTopology:true });


module.exports = mongoose;
