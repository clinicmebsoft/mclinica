let espanol={
            paginate: {
                first: " |< ",
                previous: "Ant.",
                next: "Sig.",
                last: " >| "
            },
            emptyTable:			"No hay datos disponibles en la tabla.",
            info:		   		"Del _START_ al _END_ de _TOTAL_ ",
            infoEmpty:			"Mostrando 0 registros de un total de 0.",
            infoFiltered:			"(filtrados de un total de _MAX_ registros)",
            infoPostFix:			"(actualizados)",
            lengthMenu:			"Mostrar _MENU_ registros",
            loadingRecords:		"Cargando...",
            processing:			"Procesando...",
            searchPlaceholder:		"Buscar ",
            zeroRecords:			"No se han encontrado coincidencias.",
            search: 				"Buscar:" ,
            processing: "Procesando la información",
            select: {
                rows: "%d Registros Seleccionados"
            }
        }



/* se tiene que incluir en producto.html {% include 'catalogo/mod_unidad.html' %}*/

document.getElementById("btnCategoria").addEventListener("click",function(){
    $('#modalCatalogoCategorias').modal('show');
    cargaTablas('#tCataCategoria','ajax_catalogo_listcategoria','iCataCategoria','iIdCate');
})
document.getElementById("btnUnidad").addEventListener("click",function(){
    $('#modalCatalogoUnidad').modal('show');
    cargaTablas('#tCataUnidad','ajax_catalogo_unidad','iCataUnidad','iIdUnidad');
})
document.getElementById("btnMarca").addEventListener("click",function(){
    $('#modalCatalogoMarca').modal('show');
    cargaTablas('#tCataMarca','ajax_catalogo_marca','iCataMarca','iIdMarca');
})

document.getElementById("btnFabricante").addEventListener("click",function(){
    $('#modalCatalogoFabricante').modal('show');
    cargaTablas('#tCataFabricante','ajax_catalogo_fabricante','iCataFabricante','iIdFabricante');
})
document.getElementById("btnImpuesto").addEventListener("click",function(){
    $('#modalCatalogoImpuesto').modal('show');
    cargaTablas('#tCataImpuesto','ajax_catalogo_impuesto','iCataImpuesto','iIdImpuesto');
})
// ___________________ General __________________
function cargaTablas(pTabla, pUrl, pCampoDescrip,pCampoId){
    let columnas = [];
    if (pUrl!="ajax_catalogo_impuesto"){
        columnas = [

                {"data":"id", width:'20%'},
                {"data":"descripcion", width:'60%'},
                {"data":"estatus", width:'20%'},
            ]
		}else{
		    columnas = [

                {"data":"id", width:'15%'},
                {"data":"descripcion", width:'55%'},
                {"data":"porcentaje", width:'15%'},
                {"data":"estatus", width:'15%'},
            ]

		}
    $(document).ready(function() {
    let tabla= $(pTabla).DataTable({
       destroy: true,
       autoWidth : false,
       buttons: [
            'selectRows',
            'selectColumns',
            'selectCells'
        ],
       columnDefs: [ {
            orderable: false,
            className: 'select-checkbox',
            targets:   0
        } ],
        select: {
            style:    'os',
            selector: 'td:first-child'
        },
        order: [[ 1, 'asc' ]],
        autoFill: {
            columns: ':not(:first-child)'
        },
        language : espanol,
        "scrollY": "200px",
        "ajax" : {
            url : pUrl,
            dataSrc : "data",
            type : "GET"
        },
		columns: columnas
    });
     let id = document.getElementById(pCampoId);
     let icat = document.getElementById(pCampoDescrip);
     let porcen = document.getElementById('iCataPorcentaje');
    var table = $(pTabla).DataTable();
        $(pTabla +' tbody').on('click', 'tr', function () {
            if ($(this).hasClass('selected')) {
                $(this).removeClass('selected');
                id.value ="";
                icat.value = "";
                porcen.value = "";
            }
            else {
                $(pTabla+' tr.selected').removeClass('selected');
                $(this).addClass('selected');
                 let row = tabla.row( $(this) ).data();
                id.value = row['id'];
                icat.value = row['descripcion'];
                if (pUrl=="ajax_catalogo_impuesto"){
                   porcen.value = row['porcentaje'];
                }
            }

        });

  } );
}

function limpiaUnidad()
{
    $('#iCataUnidad').val('');
    $('#iId').val('');
    $('#iCataUnidad').focus();
}
function limpiaCategorias()
{
    $('#iCataCategoria').val('');
    $('#iId').val('');
    $('#iCataCategoria').focus();
}
function limpiaMarcas()
{
    $('#iCataMarca').val('');
    $('#iId').val('');
    $('#iCataCategoria').focus();
}
function limpiaFabricantes()
{
    $('#iCataMarca').val('');
    $('#iId').val('');
    $('#iCataCategoria').focus();
}

function limpiaImpuesto()
{
    $('#iCataMarca').val('');
    $('#iId').val('');
    $('#iCataImpuesto').focus();
    $('#iCataPorcentaje').val("");
}
function tipoCatalogo(cual){
    if (cual=='Unidades'){return "#iCataUnidad";}
    if (cual=='Categorias'){return "#iCataCategoria";}
    if (cual=='Marcas'){return "#iCataMarca";}
    if (cual=='Fabricantes'){return "#iCataFabricante";}
    if (cual=='Impuestos'){return "#iCataImpuesto";}
}

function guardaCatalogos(que,tipo,id){
    //alert(que + " "+tipo);
    let dTipo = $(tipoCatalogo(tipo)).val();
    id = $('#'+id).val();
    if (que=='G'){id=0;}
    if (tipo!="Impuestos"){
        datos = {
            'descripcion' : dTipo,
            'tipo' : tipo,
            'que' : que,
            'id' : id
        }
    } else{
        let porcen = document.getElementById("iCataPorcentaje").value;
        datos = {
            'descripcion' : dTipo,
            'tipo' : tipo,
            'que' : que,
            'id' : id,
            'porcentaje': porcen
            }
    }
    if (dTipo == ''){
        toastr.warning("Falta "+tipo+"...");
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
            url : 'ajax_abcGuardarCatalogos',
            success : function(resultado) {
            //alert(resultado.respuesta.mensaje);
        	if (resultado.respuesta.mensaje.includes("Error") ){
        	    toastr.error(resultado.respuesta.mensaje)
        		}
        	else{
                toastr.success(resultado.respuesta.mensaje);
                tipoCatalogo(tipo)
                switch(tipo)
                {
                    case 'Unidades':
                        //cargaTablas('#tCataUnidad','ajax_catalogo_unidad','iCataUnidad','iIdUnidad');
                        $('#tCataUnidad').DataTable().ajax.reload();
                        limpiaUnidad();
                        iSelect("#sUnidad","ajax_catalogo_unidad");
                        break;
                    case 'Categorias':
                        //cargaTablas('#tCataCategoria','ajax_catalogo_listcategoria','iCataCategoria','iIdCate');
                        $('#tCataCategoria').DataTable().ajax.reload();
                        limpiaCategorias();
                        iSelect("#sCategoria","ajax_catalogo_listcategoria"); //carga en select option
                        break;
                    case 'Marcas':
                        //cargaTablas('#tCataMarca','ajax_catalogo_marca','iCataMarca','iIdMarca');
                        $('#tCataMarca').DataTable().ajax.reload();
                        limpiaMarcas();
                        iSelect("#sMarcas","ajax_catalogo_marca"); //carga en select option
                        break;
                     case 'Fabricantes':
                        $('#tCataFabricante').DataTable().ajax.reload();
                       // cargaTablas('#tCataFabricante','ajax_catalogo_fabricante','iCataFabricante','iIdFabricante');
                        limpiaFabricantes();
                        iSelect("#sFabricante","ajax_catalogo_fabricante"); //carga en select option
                        break;
                     case 'Impuestos':
                        $('#tCataImpuesto').DataTable().ajax.reload();
                       // cargaTablas('#tCataImpuesto','ajax_catalogo_impuesto','iCataImpuesto','iIdImpuesto');
                        limpiaFabricantes();
                        iSelect("#sImpuessto","ajax_catalogo_impuesto"); //carga en select option
                        break;
                    default:
                        console.log('Error : no encontré opción switch');
                }
        	}
            },
          })
      }
}
