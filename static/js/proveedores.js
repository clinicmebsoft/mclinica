function EsVacio(campo){
	return campo == null || campo === "";
}
let datos={}
let pasa=false;
function tomaValoresFormulario(){
    datos={
        "razonSocial" : $('#iProvRazonSocial').val(),
        "nombre" : $('#iProvNombre').val(),
        "apellidoPat" : $('#iProvApellidoPat').val(),
        "apellidoMat ": $('#iProvApellidoMat').val(),
        "cp ": $('#iProvCP').val(),
        "estado  ": $('#iProvCP').val(),
        "ciudad ": $('#iProvCiudad').val(),
        "municipio ": $('#iProvMunicipio').val(),
        "colonia ": $('#iProvColonia option:selected').text(),
        "calle ": $('#iProvCalle').val(),
        "telefono ": $('#iProvTelefono').val(),
        "celular ": $('#iProvCelular').val(),
        "email  ": $('#iProvEmail').val(),
        "pagina ": $('#iProvPaginaWeb').val(),
        "observaciones ": $('#iProvObservaciones').val(),
    }


    if(datos.nombre===""){
        pasa=false;
    }
    //if (datos['razonSocial'])
}
function guardaProveedor(que){
    alert(que);
    tomaValoresFormulario();
    if (pasa===true)
    {
        if (que=='C'){

        }else{
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
                        tipoCatalogo(tipo);
                    }
                }
              })
        }
   }
}

