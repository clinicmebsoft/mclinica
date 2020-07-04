
let datos={}
let pasa=true;
function tomaValoresFormulario(que){
    datos={
        "tipo" : $('#iProvRazonSocial').val(),
        "codigo" : $('#iProvNombre').val(),
        "descripcion" : $('#iProvApellidos').val(),
        "codigobarras": $('#iProvCP').val(),
        "id_categoria": $('#iProvCP').val(),
        "id_unidades": $('#iProvCiudad').val(),
        "id_marcas": $('#iProvMunicipio').val(),
        "id_fabricantes": $('#iProvColonia option:selected').text(),
        "precioventa": $('#iProvCalle').val(),
        "costo": $('#iProvTelefono').val(),
        "stock_min": $('#iProvCelular').val(),
        "stock_max": $('#iProvEmail').val(),
        "reorden": $('#iProvPaginaWeb').val(),
        "cantidad": $('#iProvObservaciones').val(),
        "id_impuestos" : $('#sImpuesto'),
        "id_proveedores" : $('#sProveedor'),
        "compuesto" : $('#cCompuesto'),
        //"id_compuesto" : $('#')


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

function guardarArticulo(){
    tomaValoresFormulario(que);
    if (pasa===true)
    {
    }
}