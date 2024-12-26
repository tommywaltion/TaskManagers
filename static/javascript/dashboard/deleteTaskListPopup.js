let taskListIdToDelete = null;

const TaskListTableParent = document.getElementById('taskList-table-container');

TaskListTableParent.addEventListener('click', function(event) {
    if (event.target && event.target.matches('button.delete-task-list-btn')) {
        const btn = event.target;
        taskListIdToDelete = btn.getAttribute('data-task-list-id');
        const taskListName = btn.closest('.task-list').querySelector('h2').textContent;

        taskTitleElement.textContent = taskListName + " ?";
        popup.style.display = 'block';
        overlay.style.display = 'block';
    }
});

confirmDeleteBtn.addEventListener('click', function () {
    if (taskListIdToDelete) {
        fetch("/delete_list/", {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrf_token,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ tasklist_id: taskListIdToDelete})
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                //alert('Tasklist deleted successfully');
                const deleteTaskList = document.querySelector(`div[data-task-list-id="${taskListIdToDelete}"]`);
                if (deleteTaskList) deleteTaskList.remove();
            } else {
                alert("error: " + data.error);
            }
        })
        .catch(error => console.error("Error:", error))
        .finally(() => {
            taskListIdToDelete = null;
            popup.style.display = 'none';
            overlay.style.display = 'none';
        });
    };
});

cancelDeleteBtn.addEventListener('click', function (event) {
    event.preventDefault();
    taskListIdToDelete = null;
    popup.style.display = 'none';
    overlay.style.display = 'none';
});