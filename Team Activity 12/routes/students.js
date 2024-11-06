var express = require('express');
var router = express.Router();
var Student = require("../models/student");

// CRUD implementation

router.post("/create", function (req, res) {
    const newStudent = new Student({
        name: req.body.name,
        major: req.body.major,
        gpa: req.body.gpa
    });
    newStudent.save(function (err, student) {
        if (err) {
            res.status(400).send(err);
        }
        else {
            let msgStr = `Student (${req.body.name}) info has been saved.`;
            res.status(201).json({ message: msgStr });
            console.log(msgStr);
        }
    });

});

router.post("/delete", function(req, res) {
    Student.deleteOne({ name: req.body.name }, function(err, doc) {
        if (err) {
            let msgStr = `Error: ${err}`;
            res.status(201).json({ message: msgStr });
        }
        else {
            if (doc.n === 0) {
                let msgStr = `Student (${req.body.name}) not found.`;
                res.status(200).json({ message: msgStr });
                console.log(msgStr);
            }
            else {
                let msgStr = `Student (${req.body.name}) info has been deleted.`;
                res.status(200).json({ message: msgStr });
                console.log(msgStr);
            }
        }
    });
});
// router.post("/update", function (req, res) {
//     Student.findOneAndUpdate({ name: req.body.name }, function (err, doc) {
//         if (err) {
//             let msgStr = `Error: ${err}`;
//             res.status(201).json({ message: msgStr });
//         }
//         else {
//             if (doc === null) {
//             let msgStr = `Student (${req.body.name}) info has been updated.`;
//             res.status(200).json({ message: msgStr });
//             console.log(msgStr);
//         }
//     }

router.get('/readAll', function(req, res) {
    Student.find({}, function(err, docs) {
        if (err) {
            let msgStr = `Error: ${err}`;
            res.status(201).json({ message: msgStr });

        }
        else {
            res.status(200).json(docs);
        }
    });
});

router.get("/count", function (req, res) {
    Student.estimatedDocumentCount(function (err, count) {
        if (err) {
            let msgStr = `Error: ${err}`;
            res.status(201).json({ message: msgStr });
        }
        else {
            res.status(200).json({ count: count });
        }
    });
});

module.exports = router;