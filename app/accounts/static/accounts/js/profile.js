const params = new URLSearchParams(window.location.search);
const userName = params.get('user')

const userNotFound = document.getElementById('user-not-found')
const userInfoBar = document.getElementById('user-info-bar')
const threadHighlights = document.getElementById('thread-highlights')

const resetDisplay = () => {
    userNotFound.dataset.active = "false"
    userInfoBar.dataset.active = "true"
}

const noUser = () => {
    userNotFound.dataset.active = "true"
    userInfoBar.dataset.active = "false"
}

/**
 * Gets User information from the sample users.json file
 * and populates the appropriate fields with the information.
 * If no user is found then the page will update to notify the user.
 * 
 * @param {string} userKey 
 */
const loadUser = async (userKey) => {
    noUser();

    if (!userKey) { return; }

    try {

        const response = await fetch('https://raw.githubusercontent.com/Seth-Browning/CSC321-Midterm/main/data/users.json');
        const users = await response.json();

        const user = users[userKey]
        if (!user) {
            noUser()
            return;
        }

        resetDisplay()

        document.title = `${userKey}'s Profile`

        document.getElementById('user-name').innerText = userKey;
        document.getElementById('user-joined').innerText = `Joined: ${user.joined}`
        document.getElementById('user-bio').innerText = user.bio
        document.getElementById('user-followers').innerText = user.observes_number
        document.getElementById('user-following').innerText = user.observed_by_number

    } catch (err) {
        console.error(err)
        noUser()
    }
}

/**
 * 
 * @param {string} userId 
 */
const loadThreads = async (userId) => {
    if (!userId) return;

    try {

        const request = await fetch('https://raw.githubusercontent.com/Seth-Browning/CSC321-Midterm/main/data/threads.json')
        const allThreads = await request.json();

        console.log(allThreads)
        // const threadsFromUser = allThreads.filter((threadObj) => threadObj.poster === userId)
        // const threadElements = allThreads.forEach((thread) => {
        //     threadHighlights.insertAdjacentHTML('beforeend', `<thread-highlight title="${thread.title}" thread-id="${thread}" user-name=${thread.poster}></thread-highlight>`)
        // })

        Object.keys(allThreads).forEach(thread => {
            console.log(thread)
            if(allThreads[thread].poster == userId) {
                const th = allThreads[thread]
                threadHighlights.insertAdjacentHTML('beforeend', `<thread-highlight title="${th.title}" thread-id="${thread}" user-name="${th.poster}"></thread-highlight>`)
            }
        })

    } catch (error) {
        console.error(error)
    }
}


(async function() {
    loadUser(userName)
    loadThreads(userName)
})();