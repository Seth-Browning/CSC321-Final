
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
        'register-link',
    ]

    constructor() {
        super();
    }

    connectedCallback() {
        
        const loggedIn = this.getAttribute('logged-in') ?? 'False'
        const username = this.getAttribute('username') ?? ''

        const homeLink = this.getAttribute('home-link') ?? '/'
        const loginLink = this.getAttribute('login-link') ?? '/'
        const registerLink = this.getAttribute('register-link') ?? '/'

        let navBarOptions;

        // the loggedIn property is set by the renderer in python, so the boolean as a string
        // will be capitalized instead of lowercase
        if (loggedIn === "True") {
            navBarOptions = `
            <div id="logged-in-options" class="nav-log-dependent" data-active="true">
                <div class="nav-dropdown">
                    <p class="logged-in-username">${username}</p>
                    <div class="nav-dropdown-content">
                        <a>Settings</a>
                        <a href="/accounts/logout">Log out</a>
                    </div>
                </div>
            </div>` 
        } else {
            navBarOptions = `
            <div id="log-in-options" class="nav-log-dependent" data-active="true">
                <button class="primary-button to-login">Log In</button>
                <button class="secondary-button to-signup">Sign Up</button>
            </div>`
        }

        this.innerHTML = `
            <nav>
                <div id="nav-bar-left">
                    <p class="home-page-link">
                        <a href="${homeLink}">Games Forum</a>
                    </p>
                </div>
                ${ navBarOptions }
            </nav>`


        this.querySelector('.to-login')?.addEventListener('click', () => {
            window.location.href = loginLink
        })

        this.querySelector('.to-signup')?.addEventListener('click', () => {
            window.location.href = registerLink
        })

        this.querySelector('.logged-in-username')?.addEventListener('click', () => {
            window.location.href = `/accounts/profile/${username}/`
        })
    }
}

customElements.define("nav-bar", NavBar);