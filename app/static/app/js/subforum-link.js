
class SubforumLink extends HTMLElement {
    static observedAttributes = [
        'subforum',
        'display-name'
    ]
    
    constructor() {
        super()
    }

    connectedCallback() {
        const subforum = this.getAttribute('subforum') ?? '';
        const displayName = this.getAttribute('display-name') ?? subforum;

        this.innerHTML = `
            <div class="subforum">${displayName}</div>
        `

        if (subforum !== '') {
            this.addEventListener('click', () => {
                window.location.href = subforum
            })
        }
    }
}

customElements.define('subforum-link', SubforumLink)