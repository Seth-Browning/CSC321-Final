class ThreadHighlight extends HTMLElement {
    static observedAttributes = [
        "user-name",
        "title",
        "thread-id"
    ]

    constructor() {
        super()
    }

    connectedCallback() {
        const title = this.getAttribute('title')
        const poster = this.getAttribute('user-name')
        const threadId = this.getAttribute('thread-id')

        this.innerHTML = `
            <style>
                
            </style>

            <div class="thread">
                <div class="thread-top">
                    <p class="thread-title">${title}</p>
                    <p class="thread-creator">${poster}</p>
                </div>
            </div>
        `

        this.querySelector('.thread-title').addEventListener('click', () => {
            window.location.href = `thread.html?id=${threadId}`
        })

        this.querySelector('.thread-creator').addEventListener('click', () => {
            window.location.href = `profile.html?user=${poster}`
        })
    }
}

customElements.define('thread-highlight', ThreadHighlight)