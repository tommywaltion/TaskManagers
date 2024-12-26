const statusDropdowns = document.querySelectorAll('.task-status');

    statusDropdowns.forEach(dropDown => {
        dropDown.addEventListener('change', function () {
            const taskId = this.getAttribute('data-task-id'); // Get task ID
            const newStatus = this.value;

            fetch(`/update/${taskId}/`, {
                method: 'POST',
                headers: {
                        'X-CSRFToken': csrf_token,
                        'Content-Type': 'application/json',
                    },
                body: JSON.stringify({
                    status: newStatus,
                }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    //alert('Task Status updated successfully');
                    const taskRow = document.querySelector(`tr[data-task-id="${taskId}"]`);
                    const statusBox = taskRow.querySelector('.status-box');
                    if (statusBox){
                        statusBox.classList.remove("todo-box");
                        statusBox.classList.remove("progress-box");
                        statusBox.classList.remove("complete-box");
                        statusBox.classList.add(getStatusColor(newStatus));
                    }
                } else {
                    alert('Failed to update task status')
                }
            })
            .catch(error => {
                console.error('Error: ', error);
                alert('An error occured while updating task status')
            })
        })
    })

    function getStatusColor(status) {
        switch (status) {
            case "To Do":
                return "todo-box";
            case "In Progress":
                return "progress-box";
            case "Completed":
                return "complete-box";
            default:
                return "";
        }
    }