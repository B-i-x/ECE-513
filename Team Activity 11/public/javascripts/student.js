// public/javasciprts/student.js

function createStudent() {
    // data validation
    if ($('#name').val() === "") {
        window.alert("invalid name!");
        return;
    }
    if ($('#major').val() === "") {
        window.alert("invalid major!");
        return;
    }
    if ($('#gpa').val() === "") {
        window.alert("invalid gpa!");
        return;
    }

    let txdata = {
        name: $('#name').val(),
        major: $('#major').val(), 
        gpa: Number($('#gpa').val())
    };

    $.ajax({
        url: '/students/create',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(txdata),
        dataType: 'json'
    })
    .done(function (data, textStatus, jqXHR) {
        $('#rxData').html(JSON.stringify(data, null, 2));
    })
    .fail(function (data, textStatus, jqXHR) {
        $('#rxData').html(JSON.stringify(data, null, 2));
    });
}

function readStudent() {
    /* your code here */
}

function updateStudent() {
    // data validation
    if ($('#name').val() === "") {
        window.alert("invalid name!");
        return;
    }
    if ($('#major').val() === "") {
        window.alert("invalid major!");
        return;
    }
    if ($('#gpa').val() === "") {
        window.alert("invalid gpa!");
        return;
    }

    let txdata = {
        name: $('#name').val(),
        major: $('#major').val(), 
        gpa: $('#gpa').val()
    };

    $.ajax({
        url: '/students/update',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(txdata),
        dataType: 'json'
    })
    .done(function (data, textStatus, jqXHR) {
        $('#rxData').html(JSON.stringify(data, null, 2));
    })
    .fail(function (data, textStatus, jqXHR) {
        $('#rxData').html(JSON.stringify(data, null, 2));
    });
}

function deleteStudent() {
    /* your code here */
}

function getCount() {
    $.ajax({
        url: '/students/count',
        method: 'GET'
    })
    .done(function (data, textStatus, jqXHR) {
        $('#rxData').html(JSON.stringify(data, null, 2));
    })
    .fail(function (data, textStatus, jqXHR) {
        $('#rxData').html(JSON.stringify(data, null, 2));
    });
}

function readAll() {
    /* your code here */
    
}

function searchStudent() {
    // data validation
    if ($('#gpa').val() === "") {
        window.alert("invalid gpa!");
        return;
    }
    
    let txdata = {
        gpa: Number($('#gpa').val())
    };

    $.ajax({
        url: '/students/search',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(txdata),
        dataType: 'json'
    })
    .done(function (data, textStatus, jqXHR) {
        $('#rxData').html(JSON.stringify(data, null, 2));
    })
    .fail(function (data, textStatus, jqXHR) {
        $('#rxData').html(JSON.stringify(data, null, 2));
    });
}


$(function () {
    $('#btnCreate').click(createStudent);
    $('#btnRead').click(readStudent);
    $('#btnUpdate').click(updateStudent);
    $('#btnDelete').click(deleteStudent);
    $('#btnCount').click(getCount);
    $('#btnReadAll').click(readAll);
    $('#btnSearch').click(searchStudent);
});