function openEditModal(id, name) {
    const modal = document.getElementById('editTaskListModal');
    const taskListNameInput = document.getElementById('taskListName');
    const taskListIdInput = document.getElementById('taskListId');


    taskListNameInput.value = name;
    taskListIdInput.value = id;

    modal.style.display = 'block';
    overlay.style.display = 'block';
}

function closeEditModal() {
    const modal = document.getElementById('editTaskListModal');
    modal.style.display = 'none';
    overlay.style.display = 'none';
}

function saveTaskList() {
    const taskListName = document.getElementById('taskListName').value;
    const taskListId = document.getElementById('taskListId').value;

    fetch('/update_tasklist/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrf_token,
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            id: taskListId,
            name: taskListName,
        }),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        if(data.success) {
            // alert('TaskList updated successfully');
            location.reload();
        } else {
            alert('An error occured, please try again');
        }
    })
    .catch(error => {
        console.error('error', error);
        alert('an error occured, please try again');
    });
}