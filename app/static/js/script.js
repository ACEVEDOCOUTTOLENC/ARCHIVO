// Simulamos una base de datos con registros
const records = [
    { id: 1, name: 'Juan Pérez', email: 'juan@example.com' },
    { id: 2, name: 'Ana García', email: 'ana@example.com' },
    { id: 3, name: 'Carlos Rodríguez', email: 'carlos@example.com' },
    { id: 4, name: 'Laura Gómez', email: 'laura@example.com' },
    { id: 5, name: 'Pedro López', email: 'pedro@example.com' }
];

// Función para mostrar los registros en la lista
function displayRecords(filteredRecords) {
    const recordList = document.getElementById('recordList');
    recordList.innerHTML = ''; // Limpiar lista antes de agregar los nuevos resultados

    filteredRecords.forEach(record => {
        const li = document.createElement('li');
        li.textContent = `${record.name} - ${record.email}`;
        recordList.appendChild(li);
    });
}

// Función de búsqueda de registros
function searchRecords() {
    const searchInput = document.getElementById('searchInput').value.toLowerCase();
    const filteredRecords = records.filter(record => {
        return record.name.toLowerCase().includes(searchInput) || record.email.toLowerCase().includes(searchInput);
    });

    displayRecords(filteredRecords); // Muestra los registros filtrados
}

// Al cargar la página, mostramos todos los registros
window.onload = () => {
    displayRecords(records);
};
