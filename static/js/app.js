const form = document.getElementById("form");
const btnAdd = document.getElementById("btn-add");
const cancelar = document.getElementById("cancelar");

document.querySelectorAll(".btn-edit").forEach((btn) => {
    btn.addEventListener("click", () => {
        form.action = "/editar/" + btn.dataset.id;
        form.nombre.value = btn.dataset.nombre;
        form.especie.value = btn.dataset.especie;
        form.color.value = btn.dataset.color;
        btnAdd.textContent = "Guardar";
        cancelar.hidden = false;
        form.nombre.focus();
    });
});