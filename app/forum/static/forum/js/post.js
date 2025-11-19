const whereToPost = document.getElementById('where-to-post')

const succcessBar = document.getElementById('post-status-success')
const failBar = document.getElementById('post-status-fail')

document.querySelector('text-editor').addEventListener('text-editor-submit', (e) => {
    console.log('fired')
    if (e.detail.text.trim() === '') return;

    const randomNumber = Math.floor(Math.random() * 100)
    console.log(randomNumber)
    const failRate = 10

    if (randomNumber >= failRate) {
        succcessBar.dataset.active = "true"
        e.target.clearText()
        setTimeout(() => {succcessBar.dataset.active = 'false'}, 2500)
    } else {
        failBar.dataset.active = "true"
        setTimeout(() => {failBar.dataset.active = 'false'}, 2500)
    }

})