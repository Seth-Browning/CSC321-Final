
if (!localStorage.getItem('loggedInUser')) {
    document.getElementById('post-button').style.display = "none"
} else {
    document.getElementById('post-button').addEventListener('click', () => {
        window.location.href = 'post.html'
    })
}