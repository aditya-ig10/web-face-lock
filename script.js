function login() {
    var email = document.getElementById('Email').value;
    var password = document.getElementById('Password').value;
    if (email === 'aditya@seabirds.com' && password === 'admin1234') {
        window.location.href = 'login.html';
        return false;
    } else {
        alert('Invalid email or password');
        return false;
    }
}
function redirectSpecial() {
    window.location.href = 'http://127.0.0.1:5000';
    event.preventDefault();
}
