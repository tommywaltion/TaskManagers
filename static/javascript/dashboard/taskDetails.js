function fetchTaskDetails(taskId) {
    fetch(`/detail/${taskId}/json/`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('taskTitle').innerText = data.title;
            document.getElementById('taskDescription').innerText = data.description;
            document.getElementById('taskDueDate').innerText = data.deadline;
            document.getElementById('taskDaysLeft').innerText = data.days_left;
            document.getElementById('taskStatus').innerText = data.status;

            const daysLeftElement = document.getElementById('taskDaysLeft');
            if (data.days_left === "Overdue") {
                daysLeftElement.classList.add('overdue');
                daysLeftElement.classList.remove('highlight');
            } else {
                daysLeftElement.classList.remove('overdue');
                daysLeftElement.classList.add('highlight');
            };

            document.getElementById('taskModal').style.display = 'block';
            overlay.style.display = 'block';
        })
        .catch(error => console.error("Error fetching task details:", error));
}

function closeModal() {
    document.getElementById('taskModal').style.display = 'none';
    overlay.style.display = 'none';
}