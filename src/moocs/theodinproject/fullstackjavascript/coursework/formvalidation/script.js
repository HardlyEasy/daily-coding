const form = document.getElementById('my-form');
let validEmail = false, validZipcode = false, validPassword = false;

form.addEventListener('change', function() {
    // Email checking
    const regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (form.email.value.match(regexEmail)) {
        form.email.style.borderColor = 'black';
        validEmail = true;
    }
    else {
        form.email.style.borderColor = 'red';
    }
    // Zipcode checking
    const regexZipcode = /^\d{5}[-\s]?(?:\d{4})?$/gm;
    if (form.zipcode.value.match(regexZipcode)) {
        form.zipcode.style.borderColor = 'black';
        validZipcode = true;
    }
    else {
        form.zipcode.style.borderColor = 'red';
    }
    // Password checking
    if (form.password.value.match(form.passwordConfirm.value)
    && form.password.value != '') {
        form.password.style.borderColor = 'black';
        form.passwordConfirm.style.borderColor = 'black';
        validPassword = true;
    }
    else {
        form.password.style.borderColor = 'red';
        form.passwordConfirm.style.borderColor = 'red';
    }
})

function handleSubmit() {
    if (validEmail && validZipcode && validPassword)
        alert("Submitted successfully!")
    else
        alert("Error fields not proper")
}