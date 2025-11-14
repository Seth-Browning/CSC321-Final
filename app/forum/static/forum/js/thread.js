const params = new URLSearchParams(window.location.search)
const postId = params.get('id')

const threadContentContainer = document.getElementById('thread-content')

/**
 * 
 * @param {string} postId 
 * @returns 
 */
const loadPostContent = async (postId) => {
    if (!postId) return;

    try {
        
        const request = await fetch('https://raw.githubusercontent.com/Seth-Browning/CSC321-Midterm/main/data/threads.json')
        const allPosts = await request.json();

        const post = allPosts[postId]
        if (!post) return;

        document.getElementById('thread-title').innerText = post.title
        document.title = post.title

        const postElement = `<thread-post user-name="${post.poster}" message="${post.message}"></thread-post>`

        threadContentContainer.insertAdjacentHTML('afterbegin', postElement)

    } catch (error) {
        console.error(error)
    }
}

document.querySelector('text-editor').addEventListener('text-editor-submit', (e) => {
    const commentText = e.detail.text;
    if (commentText === '') return;
    
    e.target.clearText();
    const newComment = `<thread-post user-name="<i>Guest User</i>" message="${e.detail.text}" active="false"></thread-post>`
    threadContentContainer.insertAdjacentHTML('beforeend', newComment)
})

console.log("ran")