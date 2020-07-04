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
                $(idSelect).append( '<option value="0" selected> No Aplica </option>' );
            }else{console.log('No data '+idSelect)}
        }
    });
}

function configurarProd(){
    alert("Configurar producto");
}

