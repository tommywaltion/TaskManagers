document.querySelectorAll('.filter-priority').forEach((dropdown) => {
    dropdown.addEventListener('change', function () {
        const selectedPriority = this.value;
        const taskTable = this.closest('.task-list').querySelector('.task-table tbody');

        taskTable.querySelectorAll('tr').forEach((row) => {
            const priorityValue = row.getAttribute('data-priority-value');

            if (selectedPriority === '0') {
                row.style.display = '';
            } else if (priorityValue === selectedPriority) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
    });
});