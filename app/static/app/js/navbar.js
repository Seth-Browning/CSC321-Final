
/**
 * The main navigation bar that should only present one time in each page
 * of the website.
 */
class NavBar extends HTMLElement {
    static observedAttributes = [
        'logged-in',
        'username',
        'home-link',
        'login-link',
        'register-link'
    ]

    constructor() {
        super();
    }

    connectedCallback() {
        
        const loggedIn = this.getAttribute('logged-in') ?? 'false'
        const username = this.getAttribute('username') ?? ''
        const homeLink = this.getAttribute('home-link') ?? '/'
        const loginLink = this.getAttribute('login-link') ?? '/'
        const registerLink = this.getAttribute('register-link') ?? '/'


        this.innerHTML = `
            <nav>
                <div id="nav-bar-left">
                    <p class="home-page-link">
                        <a href="${homeLink}">Games Forum</a>
                    </p>
                </div>
                ${ loggedIn === 'True' ? `<div id="logged-in-options" class="nav-log-dependent" data-active="false">
                    <svg class="small-icon"><use href="../assets/icons/icons.svg#bell"></use></svg>
                    <svg class="icon"><use href="../assets/icons/icons.svg#circle-user"></use></svg>
                </div>` : `<div id="log-in-options" class="nav-log-dependent" data-active="true">
                    <button class="primary-button" id="to-login">Log In</button>
                    <button class="secondary-button" id="to-signup">Sign Up</button>
                </div>` }
            </nav>`

        console.log(this.innerHTML)


        this.querySelector('#to-login').addEventListener('click', () => {
            window.location.href = loginLink
        })

        this.querySelector('#to-signup').addEventListener('click', () => {
            window.location.href = registerLink
        })
    }
}

customElements.define("nav-bar", NavBar);