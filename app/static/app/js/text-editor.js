
class TextEditor extends HTMLElement {
    static observedAttributes = [
        'confirm-button-text',
        'include-title-input'
    ]

    constructor() {
        super()
    }

    connectedCallback() {
        const submitText = this.getAttribute('confirm-button-text') ?? "Submit"
        const includeTitleInput = this.getAttribute('include-title-input') ?? "false"

        let titleBarText = "";
        if (includeTitleInput === "true") {
            titleBarText = `<input type="text" placeholder="Title..." class="title-data" maxlength="200">`
        }


        this.innerHTML = `
            <div class="text-editor">
                ${titleBarText}
                <div class="editable-text-field main-data" contenteditable="true"></div>
                <div class="button-bar">
                    <button type="submit" class="primary-button">${submitText}</button>
                    <button class="danger-button">Cancel</button>
                </div>
            </div>        
        `

        this.querySelector('button[type="submit"].primary-button').addEventListener('click', () => {
            this.dispatchEvent(new CustomEvent('text-editor-submit', {
                detail: {
                    title: includeTitleInput === "true" ?  this.querySelector('.title-data').value : "",
                    text: this.querySelector('.editable-text-field.main-data').innerText
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