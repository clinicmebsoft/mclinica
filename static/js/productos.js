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

function initProductos(){
	iSelect("#sCategoria","ajax_catalogo_listcategoria");
	iSelect("#sUnidad","ajax_catalogo_unidad");
	iSelect("#sMarca","ajax_catalogo_marca");
	iSelect("#sFabricante","ajax_catalogo_fabricante");
	iSelect("#sImpuesto","ajax_catalogo_impuesto");
	iSelect("#sProveedor","ajax_catalogo_proveedores");
}

function iSelect(idSelect,ajaxLink){
    $.ajax({
        url: ajaxLink,
        dataType: 'json',
        type: 'get',
        success: function(resp){
            //alert(resp.data);
            if (resp.data != 'undefined'){
                $(idSelect).empty();
                for (let i=0 ; i< resp.data.length;i++) {
                    $(idSelect).append( '<option value="'+resp.data[i].id+'">'+
                                    resp.data[i].descripcion+'</option>' );
                }
                //$(idSelect).append( '<option value=0 selected> No Aplica </option>' );
            }else{console.log('No data '+idSelect)}
        }
    });
}

function listaArticulos(){
    $('#modalListaArticulos').modal('show');
    cargaTablaArticulos();
}

function configurarProd(){
    //alert("Configurar producto");
    $('#modalCompuesto').modal('show');
    //cargaTablaArticulos();
    'id', 'codigo', 'codigobarras', 'descripcion',
                                                                   'estatus')
    col = ['id','codigo','codigobarras','descripcion',]
    cargaTablas('tproductos','ajax_catalogo_lista_articulos',col,'id','codigo');
}
function cargaTablaArticulos(){
   alert('carga tabla');
}

function cargaTablas(pTabla, pUrlAjax,columnas[], pCampoDescrip,pCampoId){
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
        language : l_esp,
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



