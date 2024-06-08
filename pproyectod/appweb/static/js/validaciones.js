
//VALIDACIÓN REGISTRO


function validarNomApe() {

    var nombreApellido = document.getElementById("nombrereg").value;

    if (nombreApellido === "") {
        var nombreApellido = document.getElementById("nombrereg");
        nombrereg.classList.add("is-invalid");
        nombrereg.classList.remove("is-valid");

    } else {
        nombrereg.classList.add("is-valid");
        nombrereg.classList.remove("is-invalid");
    }
}

function validarPassReg() {
    var passreg = document.getElementById("passreg").value;

    if (passreg === "") {
        var passreg = document.getElementById("passreg");
        passreg.classList.add("is-invalid");
        passreg.classList.remove("is-valid");
    } else {
        var passreg = document.getElementById("passreg");
        passreg.classList.add("is-valid");
        passreg.classList.remove("is-invalid");
    }

}

function validarCoReg() {
    var correoreg = document.getElementById("correoreg").value;
    var regex = /[\w-\.]{2,}@([\w-]{2,}\.)*([\w-]{2,}\.)[\w-]{2,4}/;

    if ((regex.test($("#correoreg").val()) == false)) {

        var correoreg = document.getElementById("correoreg");
        correoreg.classList.add("is-invalid");
        correoreg.classList.remove("is-valid");

    } else if (correoreg === "") {

        var correoreg = document.getElementById("correoreg")
        correoreg.classList.add("is-invalid");
        correoreg.classList.remove("is-valid");

    } else {
        var correoreg = document.getElementById("correoreg");
        correoreg.classList.add("is-valid");
        correoreg.classList.remove("is-invalid");

    }

}


function validarRegistro() {

    validarNomApe();
    validarPassReg();
    validarCoReg();

    var nombrereg = document.getElementById("nombrereg");
    var passreg = document.getElementById("passreg");
    var correoreg = document.getElementById("correoreg");

    if (nombrereg.classList.contains("is-valid") && passreg.classList.contains("is-valid") && correoreg.classList.contains("is-valid")) {
        $('#modalExito').modal('show');
        $('#modalExito').on('hidden.bs.modal', function (e) { 
            window.location.href = "index.html"; 
          });
    }
}



//VALIDACIÓN LOGIN



function validarCorreo() {

    var correo = document.getElementById("correo").value;
    var regex = /[\w-\.]{2,}@([\w-]{2,}\.)*([\w-]{2,}\.)[\w-]{2,4}/;


    if ((regex.test($("#correo").val()) == false)) {

        var correo = document.getElementById("correo");
        correo.classList.add("is-invalid");
        correo.classList.remove("is-valid");

    } else if (correo === "") {
        var correo = document.getElementById("correo");
        correo.classList.add("is-invalid");
        correo.classList.remove("is-valid");


    } else {
        var correo = document.getElementById("correo");
        correo.classList.add("is-valid");
        correo.classList.remove("is-invalid");

    }
}


function validarPass() {

    var contrasena = document.getElementById("pass").value;

    if (contrasena === "") {
        var pass = document.getElementById("pass")
        pass.classList.add("is-invalid");
        pass.classList.remove("is-valid")
    } else {
        var pass = document.getElementById("pass")
        pass.classList.add("is-valid");
        pass.classList.remove("is-invalid")
    }
}


function validarLoginArtista() {
    validarPass();
    validarCorreo();

    var pass = document.getElementById("pass");
    var correo = document.getElementById("correo");
    if (pass.classList.contains("is-valid") && correo.classList.contains("is-valid")) {
        $('#modalExito').modal('show');
        $('#modalExito').on('hidden.bs.modal', function (e) { 
            window.location.href = "PagPrincipalUsuario.html"; 
          });
    }
}

function validarLoginAdm() {
    validarPass();
    validarCorreo();

    var pass = document.getElementById("pass");
    var correo = document.getElementById("correo");
    if (pass.classList.contains("is-valid") && correo.classList.contains("is-valid")) {
        
        $('#modalExito').modal('show');
        $('#modalExito').on('hidden.bs.modal', function (e) { 
            window.location.href = "PagPrincipalAdmin.html"; 
          });
    }
}



//VALIDACIÓN CONTACTO 


function validarNACont() {
    var nombrecont = document.getElementById("nombrecont").value;

    if (nombrecont === "") {
        var nombrecont = document.getElementById("nombrecont");
        nombrecont.classList.add("is-invalid");
        nombrecont.classList.remove("is-valid");

    } else {
        var nombrecont = document.getElementById("nombrecont");
        nombrecont.classList.add("is-valid");
        nombrecont.classList.remove("is-invalid");
    }
}

function validarCoCont() {
    var correocont = document.getElementById("correocont");

    var regex = /[\w-\.]{2,}@([\w-]{2,}\.)*([\w-]{2,}\.)[\w-]{2,4}/;


    if ((regex.test($("#correocont").val()) == false)) {

        var correocont = document.getElementById("correocont");
        correocont.classList.add("is-invalid");
        correocont.classList.remove("is-valid");
    } else if (correocont === "") {

        var correocont = document.getElementById("correocont")
        correocont.classList.add("is-invalid");
        correocont.classList.remove("is-valid");

    } else {
        var correocont = document.getElementById("correocont");
        correocont.classList.add("is-valid");
        correocont.classList.remove("is-invalid");

    }


}

function validarComCont() {

    var comentariocont = document.getElementById("comentariocont").value;

    if (comentariocont === "") {
        var comentariocont = document.getElementById("comentariocont");
        comentariocont.classList.add("is-invalid");
        comentariocont.classList.remove("is-valid");

    } else {
        var comentariocont = document.getElementById("comentariocont");
        comentariocont.classList.add("is-valid");
        comentariocont.classList.remove("is-invalid");

    }


}

function validarContacto() {

    validarNACont();
    validarCoCont();
    validarComCont();

    var nombrecont = document.getElementById("nombrecont");
    var correocont = document.getElementById("correocont");
    var comentariocont = document.getElementById("comentariocont");


    if (nombrecont.classList.contains("is-valid") && correocont.classList.contains("is-valid") && comentariocont.classList.contains("is-valid")) {
        $('#modalExito').modal('show');
        $('#modalExito').on('hidden.bs.modal', function (e) { 
            window.location.href = "index.html"; 
          });
    }

}

//VALIDACIÓN FORMULARIO 

function validarnomArtista() {

    var nombreArtista = document.getElementById("nombreArtista").value;

    if (nombreArtista === "") {
        var nombreArtista = document.getElementById("nombreArtista");
        nombreArtista.classList.add("is-invalid");
        nombreArtista.classList.remove("is-valid");
    } else {
        var nombreArtista = document.getElementById("nombreArtista");
        nombreArtista.classList.add("is-valid");
        nombreArtista.classList.remove("is-invalid");

    }
}

function validardescripArtista() {

    var descripcionArt = document.getElementById("descripcionArt").value;

    if (descripcionArt === "") {
        var descripcionArt = document.getElementById("descripcionArt");
        descripcionArt.classList.add("is-invalid");
        descripcionArt.classList.remove("is-valid");
    } else {
        var descripcionArt = document.getElementById("descripcionArt");
        descripcionArt.classList.add("is-valid");
        descripcionArt.classList.remove("is-invalid");
    }

}


function validarnombreObra() {

    var nombreObra = document.getElementById("nombreObra").value;

    if (nombreObra === "") {
        var nombreObra = document.getElementById("nombreObra");
        nombreObra.classList.add("is-invalid");
        nombreObra.classList.remove("is-valid");
    } else {
        var nombreObra = document.getElementById("nombreObra");
        nombreObra.classList.add("is-valid");
        nombreObra.classList.remove("is-invalid");
    }

}

function validardescripObra() {

    var descripObra = document.getElementById("descripObra").value;

    if (descripObra === "") {
        var descripObra = document.getElementById("descripObra");
        descripObra.classList.add("is-invalid");
        descripObra.classList.remove("is-valid");
    } else {
        var descripObra = document.getElementById("descripObra");
        descripObra.classList.add("is-valid");
        descripObra.classList.remove("is-invalid");
    }

}

function validartecnicaUsada() {

    var tecnicaUsada = document.getElementById("tecnicaUsada").value;

    if (tecnicaUsada === "") {
        var tecnicaUsada = document.getElementById("tecnicaUsada");
        tecnicaUsada.classList.add("is-invalid");
        tecnicaUsada.classList.remove("is-valid");
    } else {
        var tecnicaUsada = document.getElementById("tecnicaUsada");
        tecnicaUsada.classList.add("is-valid");
        tecnicaUsada.classList.remove("is-invalid");
    }

}

function validarprecioObra() {

    var precioObra = document.getElementById("precioObra").value;

    if (precioObra === "") {
        var precioObra = document.getElementById("precioObra");
        precioObra.classList.add("is-invalid");
        precioObra.classList.remove("is-valid");
    } else {
        var precioObra = document.getElementById("precioObra");
        precioObra.classList.add("is-valid");
        precioObra.classList.remove("is-invalid");
    }

}

function validarObra() {

    validarnomArtista();
    validardescripArtista();
    validarnombreObra();
    validardescripObra();
    validartecnicaUsada();
    validarprecioObra()

    var nombreArtista = document.getElementById("nombreArtista");
    var descripcionArt = document.getElementById("descripcionArt");
    var nombreObra = document.getElementById("nombreObra");
    var descripObra = document.getElementById("descripObra");
    var tecnicaUsada = document.getElementById("tecnicaUsada");
    var precioObra = document.getElementById("precioObra");



    if (nombreArtista.classList.contains("is-valid") && descripcionArt.classList.contains("is-valid") && nombreObra.classList.contains("is-valid") && descripObra.classList.contains("is-valid") && tecnicaUsada.classList.contains("is-valid") && precioObra.classList.contains("is-valid")) {
    
        $('#modalExito').modal('show');
        $('#modalExito').on('hidden.bs.modal', function (e) { 
            window.location.href = "ObraPublicada.html";; 
          });
    }


}




