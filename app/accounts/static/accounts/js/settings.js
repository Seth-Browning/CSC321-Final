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