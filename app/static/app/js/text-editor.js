
class TextEditor extends HTMLElement {
    static observedAttributes = [
        'confirm-button-text'
    ]

    constructor() {
        super()
    }

    connectedCallback() {
        const submitText = this.getAttribute('confirm-button-text') ?? "Submit"

        this.innerHTML = `
            <div class="text-editor">
                <div class="editable-text-field" contenteditable="true"></div>
                <div class="button-bar">
                    <button type="submit" class="primary-button">${submitText}</button>
                    <button class="danger-button">Cancel</button>
                </div>
            </div>        
        `

        this.querySelector('button[type="submit"].primary-button').addEventListener('click', () => {
            this.dispatchEvent(new CustomEvent('text-editor-submit', {
                detail: {
                    text: this.querySelector('.editable-text-field').innerText
                }
            }))
        })

        this.querySelector('button.danger-button').addEventListener('click', () => {
            this.dispatchEvent(new CustomEvent('text-editor-cancel', {
                
            }))
        })
    }

    clearText() {
        this.querySelector('.editable-text-field').innerText = ''
    }
}

customElements.define('text-editor', TextEditor)