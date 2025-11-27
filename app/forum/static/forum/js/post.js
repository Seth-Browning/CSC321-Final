const whereToPost = document.getElementById('where-to-post')

const succcessBar = document.getElementById('post-status-success')
const failBar = document.getElementById('post-status-fail')

document.querySelector('text-editor').addEventListener('text-editor-submit', async (e) => {
    console.log( e.detail )
    if (e.detail.text.trim() === '') return;


    // create a thread
    const threadResponse = await fetch('/api/threads/', {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken
        },
        body: JSON.stringify({
            category: whereToPost.value,
            title: e.detail.title
        })
    })

    if (!threadResponse.ok) {
        return
    }

    const threadResponseData = await threadResponse.json()
    const threadId = threadResponseData.id

    // attach a post to that thread
    const postResponse = await fetch('/api/posts/', {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken
        },
        body: JSON.stringify({
            thread: threadId,
            content: e.detail.text
        })
    })

    if (!postResponse.ok) {
        return
    }

    // redirect to that thread
    window.location.href = `/forum/thread/${threadId}`
})