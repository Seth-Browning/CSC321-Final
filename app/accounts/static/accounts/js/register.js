const registerForm = document.getElementById('register-form');


registerForm.addEventListener('submit', (e) => {
    e.preventDefault()

    const username = document.getElementById('username-input').value.trim()
    console.log(username)

    localStorage.setItem('loggedInUser', username)

    window.location.href = "home.html"
})