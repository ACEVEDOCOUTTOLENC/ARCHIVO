// Función para buscar registros
function searchRecords() {
    const input = document.getElementById("searchInput").value.toLowerCase();
    const records = document.querySelectorAll(".record");

    records.forEach(record => {
        if (record.textContent.toLowerCase().includes(input)) {
            record.style.display = "block";
        } else {
            record.style.display = "none";
        }
    });
}

// Función para mostrar las acciones al seleccionar un cliente
document.querySelectorAll('.record').forEach(record => {
    record.addEventListener('click', function () {
        const actionContainer = this.querySelector('.action-container');

        // Ocultar los action-container de otros registros
        document.querySelectorAll('.action-container').forEach(container => {
            container.style.display = 'none';
        });

        // Mostrar el action-container del registro seleccionado
        actionContainer.style.display = 'block';
    });
});

// Función para manejar las acciones seleccionadas
function handleAction(selectElement, clientName) {
    const selectedAction = selectElement.value;

    if (selectedAction === "solicitar") {
        alert(`Has seleccionado 'Solicitar' para ${clientName}.`);
        // Lógica adicional para 'Solicitar' aquí
    } else if (selectedAction === "regresar") {
        alert(`Has seleccionado 'Regresar' para ${clientName}.`);
        // Lógica adicional para 'Regresar' aquí
    }
}
