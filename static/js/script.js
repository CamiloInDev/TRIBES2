// Código JavaScript para la funcionalidad del carrito y otros elementos interactivos

document.addEventListener('DOMContentLoaded', function() {
    console.log('Script cargado correctamente');
    
    // Aquí puedes agregar el código para el carrito, sliders, etc.
    
    // Ejemplo: Inicializar tooltips de Bootstrap
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});
