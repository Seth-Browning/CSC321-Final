
class SubforumLink extends HTMLElement {
    static observedAttributes = [
        'subforum'
    ]
    
    constructor() {
        super()
    }

    connectedCallback() {
        const subforum = this.getAttribute('subforum') ?? ''

        this.innerHTML = `
            <div class="subforum">${subforum}</div>
        `

        this.addEventListener('click', () => {
            window.location.href = `subforum.html?forum=${subforum}`
        })
    }
}

customElements.define('subforum-link', SubforumLink)