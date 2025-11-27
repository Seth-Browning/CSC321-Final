class ThreadHighlight extends HTMLElement {
    static observedAttributes = [
        "user-name",
        "user-profile-link",
        "title",
        "thread-link"
    ]

    constructor() {
        super()
    }

    connectedCallback() {
        const title = this.getAttribute('title')
        const poster = this.getAttribute('user-name')
        const posterProfileURL = this.getAttribute('user-profile-link') ?? "/"
        const threadLink = this.getAttribute("thread-link") ?? "/"

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
            window.location.href = threadLink
        })

        this.querySelector('.thread-creator').addEventListener('click', () => {
            window.location.href = posterProfileURL
        })
    }
}

customElements.define('thread-highlight', ThreadHighlight)