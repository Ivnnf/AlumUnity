// Popper.js
var scriptPopper = document.createElement("script");
scriptPopper.src = "https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js";
scriptPopper.integrity = "sha384-oBqDVmMz9ATKxIep9tiCxS/Z9fNfEXiDAYTujMAeBAsjFuCZSmKbSSUnQlmh/jp3";
scriptPopper.crossOrigin = "anonymous";
document.head.appendChild(scriptPopper);

// Bootstrap.js
var scriptBootstrap = document.createElement("script");
scriptBootstrap.src = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/js/bootstrap.min.js";
scriptBootstrap.integrity = "sha384-heAjqF+bCxXpCWLa6Zhcp4fu20XoNIA98ecBC1YkdXhszjoejr5y9Q77hIrv8R9i";
scriptBootstrap.crossOrigin = "anonymous";
document.head.appendChild(scriptBootstrap);

// SweetAlert
var scriptSweetAlert = document.createElement("script");
scriptSweetAlert.src = "https://cdn.jsdelivr.net/npm/sweetalert2@11";
document.head.appendChild(scriptSweetAlert);

var scriptSweetAlertAll = document.createElement("script");
scriptSweetAlertAll.src = "https://cdn.jsdelivr.net/npm/sweetalert2@11.7/dist/sweetalert2.all.min.js";
document.head.appendChild(scriptSweetAlertAll);

// jQuery
var scriptJQuery = document.createElement("script");
scriptJQuery.src = "{% static 'js/jquery-3.6.4.min.js' %}";
document.head.appendChild(scriptJQuery);

// MDB UI Kit
var scriptMDBUI = document.createElement("script");
scriptMDBUI.src = "https://cdn.jsdelivr.net/npm/mdb-ui-kit@3.6.0/dist/mdb.min.js";
document.head.appendChild(scriptMDBUI);

// FontAwesome
var scriptFontAwesome = document.createElement("script");
scriptFontAwesome.src = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/js/all.min.js";
document.head.appendChild(scriptFontAwesome);

// Custom Icons
var scriptIcons = document.createElement("script");
scriptIcons.src = "{% static 'js/iconos.js' %}";
document.head.appendChild(scriptIcons);

// Init MDB UI
document.addEventListener("DOMContentLoaded", function() {
    const { Ripple, initMDB } = mdbui;
    initMDB({ Ripple });
});
