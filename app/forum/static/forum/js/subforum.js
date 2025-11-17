const params = new URLSearchParams(window.location.search)
const forumName = params.get('forum')

const threadList = document.getElementById('forum-posts')

const populateSubforum = async (forumName) => {
    document.title = forumName;

    try {
        const req = await fetch('https://raw.githubusercontent.com/Seth-Browning/CSC321-Midterm/main/data/threads.json')
        const jsonReq = await req.json()

        Object.keys(jsonReq).forEach(thread => {
            if (jsonReq[thread].posted_in.includes(forumName)) {
                threadList.insertAdjacentHTML('beforeend', `
                    <thread-highlight title="${jsonReq[thread].title}" user-name="${jsonReq[thread].poster}" thread-id="${thread}"></thread-highlight>
                `)
            }
        })

        document.getElementById('subforum-title').innerText = forumName

    } catch (error) {
        console.error(error)
    }

}

populateSubforum(forumName)