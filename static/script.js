
document.querySelector('#loginForm').addEventListener('submit', function(event) {
    const userId = document.getElementById('user_id').value;
    const password = document.getElementById('password').value;

    if (!userId || !password) {
        event.preventDefault();
        alert('Please fill in all fields.');
    }
});
