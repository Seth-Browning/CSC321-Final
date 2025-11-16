const loginForm = document.getElementById('login-form');

loginForm.addEventListener('submit', e => {
    e.preventDefault();

    const username = document.getElementById('username-input').value.trim();
    console.log(username);

    // This should be done only in debug mode and should NEVER grant the user
    // privaleged authority
    localStorage.setItem('loggedInUser', username);

    window.location.href = 'home.html'
})