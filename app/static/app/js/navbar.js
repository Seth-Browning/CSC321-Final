
/**
 * The main navigation bar that should only present one time in each page
 * of the website.
 */
class NavBar extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        
        this.innerHTML = `
            <nav>
                <div id="nav-bar-left">
                    <p class="home-page-link">
                        <a href="./home.html">Games Forum</a>
                    </p>
                </div>

                <div id="log-in-options" class="nav-log-dependent" data-active="true">
                    <button class="primary-button" id="to-login">Log In</button>
                    <button class="secondary-button" id="to-signup">Sign Up</button>
                </div>

                <div id="logged-in-options" class="nav-log-dependent" data-active="false">
                    <svg class="small-icon"><use href="../assets/icons/icons.svg#bell"></use></svg>
                    <svg class="icon"><use href="../assets/icons/icons.svg#circle-user"></use></svg>
                </div>
            </nav>
        `;

        this.querySelector('#to-login').addEventListener('click', () => {
            window.location.href = "login.html"
        })

        this.querySelector('#to-signup').addEventListener('click', () => {
            window.location.href = "register.html"
        })

        const user = localStorage.getItem('loggedInUser');

        if (user) {
            document.getElementById('log-in-options').dataset.active = "false"
            document.getElementById('logged-in-options').dataset.active = "true"
        } else {
            document.getElementById('log-in-options').dataset.active = "true"
            document.getElementById('logged-in-options').dataset.active = "false"
        }
    }
}

customElements.define("nav-bar", NavBar);