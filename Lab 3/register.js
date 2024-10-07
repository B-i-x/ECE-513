document.getElementById('submit').addEventListener('click', function() {
    let errors = [];
    let fullName = document.getElementById('fullName');
    let email = document.getElementById('email');
    let password = document.getElementById('password');
    let passwordConfirm = document.getElementById('passwordConfirm');
    let formErrors = document.getElementById('formErrors');

    // Reset styles and errors
    formErrors.innerHTML = '';
    formErrors.style.display = 'none';
    fullName.classList.remove('invalid');
    email.classList.remove('invalid');
    password.classList.remove('invalid');
    passwordConfirm.classList.remove('invalid');

    // Full name validation
    if (fullName.value.trim() === '') {
        errors.push("Missing full name.");
        fullName.classList.add('invalid');
    }

    // Email validation
    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,5}$/;
    if (!emailRegex.test(email.value)) {
        errors.push("Invalid or missing email address.");
        email.classList.add('invalid');
    }

    // Password validation
    if (password.value.length < 10 || password.value.length > 20) {
        errors.push("Password must be between 10 and 20 characters.");
        password.classList.add('invalid');
    }

    if (!/[a-z]/.test(password.value)) {
        errors.push("Password must contain at least one lowercase character.");
        password.classList.add('invalid');
    }

    if (!/[A-Z]/.test(password.value)) {
        errors.push("Password must contain at least one uppercase character.");
        password.classList.add('invalid');
    }

    if (!/\d/.test(password.value)) {
        errors.push("Password must contain at least one digit.");
        password.classList.add('invalid');
    }

    // Confirm password validation
    if (password.value !== passwordConfirm.value) {
        errors.push("Password and confirmation password don't match.");
        passwordConfirm.classList.add('invalid');
    }

    // Display errors if there are any
    if (errors.length > 0) {
        formErrors.style.display = 'block';
        let errorList = document.createElement('ul');
        errors.forEach(function(error) {
            let li = document.createElement('li');
            li.textContent = error;
            errorList.appendChild(li);
        });
        formErrors.appendChild(errorList);
    }
});
