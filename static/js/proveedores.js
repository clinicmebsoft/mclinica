function EsVacio(campo){
	return campo == null || campo === "";
}
let datos={}
let pasa=true;
function tomaValoresFormulario(que){
    datos={
        "razon_social" : $('#iProvRazonSocial').val(),
        "nombre" : $('#iProvNombre').val(),
        "apellidos" : $('#iProvApellidos').val(),
        "cp": $('#iProvCP').val(),
        "estado": $('#iProvCP').val(),
        "ciudad": $('#iProvCiudad').val(),
        "municipio": $('#iProvMunicipio').val(),
        "colonia": $('#iProvColonia option:selected').text(),
        "calle": $('#iProvCalle').val(),
        "telefono": $('#iProvTelefono').val(),
        "celular": $('#iProvCelular').val(),
        "email": $('#iProvEmail').val(),
        "web": $('#iProvPaginaWeb').val(),
        "observaciones": $('#iProvObservaciones').val(),
        "tipo" : que
    }

    if(datos.nombre===""){$('#iProvNombre').focus();toastr.warning('Falta Nombre...');pasa=false;return;}
    if(datos.apellidoPat===""){$('#apellidos').focus();toastr.warning('Faltan Apellidos...');pasa=false;return;}
    if(datos.cp===""){$('#iProvCP').focus();toastr.warning('Falta Código Postal...');pasa=false;return;}
    if(datos.calle===""){$('#iProvCalle').focus();toastr.warning('Falta Calle...');pasa=false;return;}
    if(datos.telefono===""){$('#iProvTelefono').focus();toastr.warning('Falta Teléfono...');pasa=false;return;}
    if(datos.email===""){$('#iProvEmail').focus();toastr.warning('Falta email...');pasa=false;return;}
    //if (datos['razonSocial'])
}

function limpiarProveedores(){
    $('#iProvRazonSocial').val("");
    $('#iProvNombre').val("");
    $('#iProvApellidos').val("");
    $('#iProvCP').val("");
    $('#iProvCP').val("");
    $('#iProvCiudad').val("");
    $('#iProvMunicipio').val("");
    $('#iProvColonia option:selected').text("");
    $('#iProvCalle').val("");
    $('#iProvTelefono').val("");
    $('#iProvCelular').val("");
    $('#iProvEmail').val("");
    $('#iProvPaginaWeb').val("");
    $('#iProvObservaciones').val("");
}

function guardaProveedor(que){
    //alert(que);
    tomaValoresFormulario(que);
    if (pasa===true)
    {
        let csrftoken = $("[name=csrfmiddlewaretoken]").val();
        $.ajax({
            type: 'POST',
            processData: false,
            contentType: "application/json",
            dataType : 'json',
            headers:{
                "X-CSRFToken": csrftoken,
                "X-Requested-With": "XMLHttpRequest"
            },
            async: false,
            data : JSON.stringify(datos),
            url : 'ajax_abcGuardarProveedor',
            success : function(resultado) {
                if (resultado.respuesta.mensaje.includes("Error") ){
                    toastr.error(resultado.respuesta.mensaje)
                    }
                else{
                    toastr.success(resultado.respuesta.mensaje);
                    limpiarProveedores();
                }
            }
          })

   }
}

