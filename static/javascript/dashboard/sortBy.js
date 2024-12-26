const sortDropDown = document.querySelectorAll('#sort-tasks');

sortDropDown.forEach((dropdown) => {
    const table = dropdown.closest('.task-list').querySelector('tbody');

    dropdown.value = 'deadline_asc';
    sortTable(table, 'deadline_asc');

    dropdown.addEventListener("change", function () {
        const sortBy = this.value;
        sortTable(table, sortBy);
    });
});

function sortTable(table, sortBy) {
    const rows = Array.from(table.rows);

    rows.sort((a,b) => {
        if (sortBy === 'deadline_asc') {
            return new Date(a.getAttribute('data-deadline')) - new Date(b.getAttribute('data-deadline'));
        } else if (sortBy === 'deadline_desc') {
            return new Date(b.getAttribute('data-deadline')) - new Date(a.getAttribute('data-deadline'));
        } else if (sortBy === 'priority') {
            const priorityA = parseInt(a.getAttribute('data-priority-value'), 10);
            const priorityB = parseInt(b.getAttribute('data-priority-value'), 10);

            if (priorityA !== priorityB) {
                return priorityB - priorityA
            }

            return new Date(a.getAttribute('data-deadline')) - new Date(b.getAttribute('data-deadline'));
        }
    });

    rows.forEach(row => table.appendChild(row));
};