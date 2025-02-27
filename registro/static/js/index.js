const subBtns = document.querySelectorAll(".sub-btn");

for (let i = 0; i < subBtns.length; i++) {
    subBtns[i].addEventListener("click", (e) => {
    e.preventDefault();
    const arrowIcon = e.currentTarget.querySelector(".arrow");
    const subMenu = e.currentTarget.nextElementSibling;
    arrowIcon.classList.toggle("rotate");
    subMenu.classList.toggle("show");
    });
}

const subBtns2 = document.querySelectorAll(".sub-btn2");

for (let i = 0; i < subBtns2.length; i++) {
    subBtns2[i].addEventListener("click", (e) => {
    e.preventDefault();
    const arrowIcon2 = e.currentTarget.querySelector(".arrow2");
    const subMenu2 = e.currentTarget.nextElementSibling;
    arrowIcon2.classList.toggle("rotate");
    subMenu2.classList.toggle("show2");
    });
}



// Code menu lateral
const menuBtn = document.querySelector('.menu-btn');
 
const sideBar = document.querySelector('.side-bar');
 
menuBtn.addEventListener('click', function() {
    sideBar.classList.add('active');
});
 
const closeBtn = document.querySelector('.close-btn');

closeBtn.addEventListener('click', function() {
    sideBar.classList.remove('active');
});


document.addEventListener('DOMContentLoaded', function() {
    const closeButtons = document.querySelectorAll('.close-btn-not');

    closeButtons.forEach((button) => {
        button.addEventListener('click', () => {
            button.parentElement.style.display = 'none';
        });
    });
});


document.addEventListener('DOMContentLoaded', function() {
    const closeButtons = document.querySelectorAll('.close-btn-not');

    closeButtons.forEach((button) => {
        button.addEventListener('click', () => {
            button.parentElement.style.display = 'none';
        });
    });
});



// Code elección de formularios

document.addEventListener("DOMContentLoaded", function () {
    const selectFormulario = document.getElementById("seleccionarFormulario");
    const secciones = document.querySelectorAll(".seccion-principal");

    // Ocultar todas las secciones al inicio usando la clase
    secciones.forEach(seccion => seccion.classList.add("hidden-custom"));

    selectFormulario.addEventListener("change", function () {
        const seleccion = selectFormulario.value;

        // Ocultar el select
        selectFormulario.classList.add("hidden-custom");

        // Mostrar solo la sección seleccionada
        secciones.forEach(seccion => {
            if (seccion.dataset.formulario === seleccion) {
                seccion.classList.remove("hidden-custom");
            } else {
                seccion.classList.add("hidden-custom");
            }
        });
    });

    // Agregar funcionalidad a los botones de cerrar
    document.querySelectorAll(".cerrar-formulario").forEach(boton => {
        boton.addEventListener("click", function () {
            // Mostrar el select nuevamente
            selectFormulario.classList.remove("hidden-custom");
            // Ocultar todos los formularios
            secciones.forEach(seccion => seccion.classList.add("hidden-custom"));
            // Reiniciar selección
            selectFormulario.value = "";
        });
    });
});