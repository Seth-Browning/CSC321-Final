
class ThreadPost extends HTMLElement {
    static observedAttributes = [
        "user-name",
        "message",
        'active',
        'profile-url'
    ]

    constructor() {
        super()
    }

    connectedCallback() {
        const name = this.getAttribute('user-name') ?? ""
        const message = this.getAttribute('message') ?? ""
        const active = this.getAttribute('active') ?? 'true';
        const profileURL = this.getAttribute('profile-url') ?? '/'

        this.innerHTML = `
            <article class="thread-entry main-post">
                <div class="user-information">
                    <h1 class="user-name">${name}</h1>
                </div>
                <div class="thread-entry-inner">
                    <header class="thread-entry-header"></header>
                    <div class="thread-entry-content">
                        <p class="thread-content-paragraph">${message}</p>
                    </div>
                    <footer class="thread-entry-footer"></footer>
                </div>
            </article>
        `
        if (active === "true") {
            this.querySelector('.user-name').addEventListener('click', () => {
                window.location.href = profileURL
            })
        }
    }
}

customElements.define("thread-post", ThreadPost)