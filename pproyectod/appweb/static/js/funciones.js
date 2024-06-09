
//ELIMINA LOS ALUMNOS DESDE LA VISTA DEL ADMIN (ListarAlmnos.HTML)
function eliminarusuario(rut_Usuario)
{
Swal.fire({
    "title": "Advertencia",
    "text": "¿Esta seguro que desea eliminar a un Usuario?",
    "icon": "question",
    "showCancelButton": true,
    "cancelButtonText": "No, cancelar",
    "confirmButtonText":"Si, eliminar"
}).then(function(result){

    if(result.isConfirmed)
    {
    window.location.href="/eliminar_usuario/"+rut_Usuario+"/";
    }

})
}


//ELIMINA LOS MODERADORES DESDE LA VISTA DEL ADMIN (ListarModerador.HTML)
function eliminarModerador(rut_Moderador)
{
Swal.fire({
    "title": "Advertencia",
    "text": "¿Esta seguro que desea eliminar a un Moderador?",
    "icon": "question",
    "showCancelButton": true,
    "cancelButtonText": "No, cancelar",
    "confirmButtonText":"Si, eliminar"
}).then(function(result){

    if(result.isConfirmed)
    {
    window.location.href="/eliminar_moderador/"+rut_Moderador+"/";
    }

})
}


//LIKE PUBLICACION ALUMNO.
function likePost(event, postId) {
    event.preventDefault(); // Prevenir el comportamiento predeterminado del enlace
    fetch(`/like/${postId}/`, {
        method: 'GET',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        document.querySelector(`#like-count-${postId}`).innerText = `${data.total_likes} likes`;
        // Actualizar el estado del checkbox
        const checkbox = document.querySelector(`#like-checkbox-${postId}`);
        checkbox.checked = !checkbox.checked;
    });
}

 // Mostrar SweetAlert al iniciar sesión//NO FUNCIONA
Swal.fire({
    title: "Bienvenido {{ request.user.username }}",
    text: "Tu sesión ha sido iniciada correctamente.",
    icon: "success",
    confirmButtonText: "Entendido"
});