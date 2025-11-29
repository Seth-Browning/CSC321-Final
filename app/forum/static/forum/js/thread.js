
document.querySelector('text-editor')?.addEventListener('text-editor-submit', async (e) => {
    
    // The variable `threadId` is populated with the current thread ID in the HTML file.

    // Send API request to add post to the current thread
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

    // redirect back to the current page to see the changes
    window.location.href = window.location.href
})
