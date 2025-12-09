const deleteModal = document.getElementById('delete-account-warning')

// Open deletion modal when the delete account button is clicked
document.getElementById('delete-account-setting').addEventListener('click', () => {
    deleteModal.showModal()
})

// close the deletion modal if the cancel button is clicked
deleteModal.querySelector('button.secondary-button').addEventListener('click', () => {
    deleteModal.close()
})

// Delete the user's account if the Confirm Deletion button is clicked
deleteModal.querySelector('button.danger-button').addEventListener('click', async () => {

    const response = await fetch(`/api/users/${CURRENT_USERNAME}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        }
    })

    if (!response.ok) {
        return
    }

    window.location.href = HOME_PAGE

})

/**
 * 
 * @param {string} category 
 */
const selectSettingCategory = (category) => {
    document.querySelectorAll('.setting-card').forEach(card => {
        card.dataset.active = "false"
        if (card.dataset.value === category) {
            card.dataset.active = "true"
        }
    })
}

document.querySelectorAll('#setting-select li').forEach(category => {
    category.addEventListener('click', () => {
        selectSettingCategory(category.dataset.value)
        document.querySelectorAll('#setting-select li').forEach(c => {
            c.classList.remove('active')
        })
        category.classList.add('active')
    })
})

const bioTextEditor = document.querySelector('#bio-text-editor')

bioTextEditor.addEventListener('text-editor-submit', async (e) => {
    const submittedText = e.detail.text

    if (submittedText.trim() === "") return;
    console.log(submittedText)

    // update bio
    const response = await fetch(`/api/users/${CURRENT_USERNAME}`, {
        method: "PUT",
        headers: {
            "Content-Type": 'application/json',
            "X-CSRFToken": csrftoken
        },
        body: JSON.stringify({
            bio: submittedText
        })
    })

    if (!response.ok) {
        console.error(response.status)
        return;
    }

    console.log("Updated")
})

// initial bio
bioTextEditor.querySelector('.main-data').innerHTML = INITIAL_BIO


document.querySelector('#change-password-button').addEventListener('click', () => {
    const dest = document.querySelector('#change-password-button').dataset.destination
    window.location.href = dest
})