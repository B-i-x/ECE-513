const db = require("../db");


/* your schema here */
const studentSchema = new db.Schema({
    name: {
        type: String,
    },
    gpa: {
        type: Number,
        min: 0,
        max: 4,
    },
    major: {
        type: String,
    }
});

const Student = db.model("Student", studentSchema);



module.exports = Student;


// references
// https://learn.zybooks.com/zybook/ARIZONAECE413SalehiFall2022/chapter/8/section/2
// https://www.geeksforgeeks.org/mongoose-estimateddocumentcount-function/ 
// https://www.geeksforgeeks.org/mongoose-find-function/
// https://www.geeksforgeeks.org/mongoose-findoneandupdate-function/
// https://www.geeksforgeeks.org/mongoose-deleteone-function/
// https://docs.mongodb.com/manual/reference/operator/query/
