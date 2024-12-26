const deleteButtons = document.querySelectorAll('.delete-btn');
let taskIdToDelete = null;
let taskNameToDelete = null;

// Show popup on delete button click
deleteButtons.forEach(button => {
    button.addEventListener('click', function () {
        taskIdToDelete = this.getAttribute('data-task-id');
        taskNameToDelete =  this.getAttribute('data-task-title');
        taskTitleElement.textContent = taskNameToDelete + " ?";
        popup.style.display = 'block';
        overlay.style.display = 'block';
    });
});

// Confirm delete button
confirmDeleteBtn.addEventListener('click', function () {
    if (taskIdToDelete) {
        fetch(`/delete/${taskIdToDelete}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrf_token,
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                const row = document.querySelector(`tr[data-task-id="${taskIdToDelete}"]`);
                if (row) {
                    row.remove();
                    //alert('Task deleted successfully!');
                } else {
                    console.error(`Row with task ID ${taskIdToDelete} not found.`);
                }
            } else {
                alert('Failed to delete task.');
            }
            taskIdToDelete = null;
        })
        .catch(error => {
            console.error('Error:', error);
        });

        popup.style.display = 'none';
        overlay.style.display = 'none';
    } 
});

cancelDeleteBtn.addEventListener('click', function (event) {
    event.preventDefault();
    taskIdToDelete = null;
    popup.style.display = 'none';
    overlay.style.display = 'none';
});