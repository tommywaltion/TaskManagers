const addTaskListBtn = document.getElementById('add-tasklist-btn');
const taskListContainer = document.getElementById('taskList-table-container');

addTaskListBtn.addEventListener('click', function () {
    const taskListName = document.getElementById('new-tasklist-name').value;

    if (taskListName.trim() === '') {
        alert('Please enter a valid Task List name');
        return;
    }

    fetch('/add_list/', {
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
            'Content-Type': 'application/json',
            },
        body: JSON.stringify({ name: taskListName })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const newTasklistName = data.name;
            const newTasklistId =  data.task_list_id;
            const newTaskList = `
            <div class="task-list" data-task-list-id="${newTasklistId}">
                <div class="tasklist-tablename">
                    <h2>${newTasklistName}</h2>
                    <div class="tasklist-action">
                        <button class="" onclick="openEditModal(${newTasklistId}, '${newTasklistName}')">
                            <i class="fa fa-pen"></i>
                        </button>
                        <a href="/create/?tasklist_id=${newTasklistId}" id="add-task">
                            <i class="fa fa-plus"></i>
                        </a>
                        <button class="delete-task-list-btn" data-task-list-id=${newTasklistId}>
                            <i class="fa fa-trash"></i>
                        </button>
                    </div>
                </div>
                <div class="filter-sort-controls">
                    <label for="">Filter by Priority:</label>
                    <select id="filter-priority">
                        <option value="0">All</option>
                        <option value="1">Low</option>
                        <option value="2">Medium</option>
                        <option value="3">High</option>
                        <option value="4">Critical</option>
                    </select>
                    <label for="">Sort by:</label>
                    <select id="sort-tasks">
                        <option value="deadline_asc" selected>Deadline (Ascending)</option>
                        <option value="deadline_desc">Deadline (Descending)</option>
                        <option value="priority">Priority</option>
                    </select>
                </div>
                <table>
                    <thead>
                        <tr>
                            <th>Status</th>
                            <th>Task Name</th>
                            <th>Due Date</th>
                            <th>Status</th>
                            <th>Priority</th>
                            <th>View</th>
                            <th>Edit</th>
                            <th>Delete</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>No item in this list</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            `;
            taskListContainer.insertAdjacentHTML('beforeend', newTaskList);
            document.getElementById('new-tasklist-name').value = "";
        } else {
            alert('error' + data.error);
        }
    });
});