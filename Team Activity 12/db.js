// to use mongoDB
const mongoose = require("mongoose");
mongoose.connect("mongodb://localhost:27017/ece413513MongoDB", { useNewUrlParser: true, useUnifiedTopology:true });


module.exports = mongoose;
