const { router } = require("../app");
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


function createStudent() {
    if($('name').val()=== ""){
        window.alert("iinvalid input");
        return;
    }
    if($('#major').val() === ""){
        window.alert("iinvalid input");
        return;
    }
    let txdata = {
        name: $('name').val(),
        major: $('major').val(),
        gpa: $('gpa').val()
    }
}

$.ajax({
    url: "/students/create",
    method: "POST",
    contentType: "application/json",
    data: JSON.stringify(txdata),
    dataType: "json",
})

router.post("/create", function (req, res) {
    const newStudent = new Student({
        name: req.body.name,
        major: req.body.major,
        gpa: req.body.gpa,
    });
});



// references
// https://learn.zybooks.com/zybook/ARIZONAECE413SalehiFall2022/chapter/8/section/2
// https://www.geeksforgeeks.org/mongoose-estimateddocumentcount-function/ 
// https://www.geeksforgeeks.org/mongoose-find-function/
// https://www.geeksforgeeks.org/mongoose-findoneandupdate-function/
// https://www.geeksforgeeks.org/mongoose-deleteone-function/
// https://docs.mongodb.com/manual/reference/operator/query/
