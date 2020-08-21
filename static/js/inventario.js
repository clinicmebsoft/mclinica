
//let datos={}
//let pasa=true;

var doc = document;
var compues = 'False';


function tomaValoresFormularioArt(que,tipo){
    if (doc.getElementById("cCompuesto").checked === true)
        compues = 'True';
    datos={
        "id" : 0,
        "tipoMov" : que,
        "tipo"  : $("input:checked").val(),
        "clave" : $("#iClaveProducto").val(),
        "descripcion" : $('#iDescripcionProducto').val(),
        "codigobarras": $("#iCodigoBarras").val(),
        "id_categoria": parseInt(doc.getElementById("sCategoria").value),
        "id_unidades": parseInt(doc.getElementById('sUnidad').value),
        "id_marcas": parseInt(doc.getElementById('sMarca').value),
        "id_fabricantes": parseInt(doc.getElementById('sFabricante').value),
        "precioventa": $("#iPrecioVenta").val(),
        "costo": $("#iPrecioCosto").val(),
        "stock_min": $("#iStockMin").val(),
        "stock_max": $("#iStockMax").val(),
        "reorden": $("#iReorden").val(),
        "cantidad": $("#iCantidad").val(),
        "id_impuestos" : parseInt(doc.getElementById('sImpuesto').value),
        "id_proveedores" : parseInt(doc.getElementById('sProveedor').value),
        "compuesto" : compues
    }

    if(datos.clave===""){$('#iClaveProducto').focus();toastr.warning('Falta Clave de Producto...');pasa=false;return;}
    if(datos.codigobarras===""){$('#iCodigoBarras').focus();toastr.warning('Falta Código de Barras...');pasa=false;return;}
    if(datos.precioventa===""){$('#iPrecioVenta').focus();toastr.warning('Falta Precio de Venta...');pasa=false;return;}
    if(datos.costo===""){$('#iPrecioCosto').focus();toastr.warning('Falta Costo...');pasa=false;return;}
    if(datos.stock_max===""){$('#iStockMax').focus();toastr.warning('Falta Stock Máximo...');pasa=false;return;}
    if(datos.stock_min===""){$('#iStockMin').focus();toastr.warning('Falta Stock Mínimo...');pasa=false;return;}
    if(datos.reorden===""){$('#iReorden').focus();toastr.warning('Punto de reorden...');pasa=false;return;}
    if(datos.cantidad===""){$('#iCantidad').focus();toastr.warning('Falta Cantidad...');pasa=false;return;}
    //if (datos['razonSocial'])
}
function guardarArticulo(que){
    let tipo = "S"
    //alert(doc.getElementById("cCompuesto").checked);

    //alert(que);
    tomaValoresFormularioArt(que,"P");
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
            url : 'ax_guardarArticulos',
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