/**
 * 
 */
//---MENU

function mensaje(enviarmensaje) {
	document.getElementById("mensaje").innerHTML=enviarmensaje;
    var x = document.getElementById("mensaje");
    x.className = "show";
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 5000);
}

var i = 0;
function tiempo_progress(){
    if(i < 100){
            i = i + 1;
            $(".progress-bar").css("width", i + "%").text(i + " %");
        }
        // Wait for sometime before running this script again
        setTimeout("tiempo_progress()", 100);
}
// tiempo_progress();

function busca_cp(cp,est,mun,ciu,call){
        datos = {
            'cp' : cp.value
        }
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        $.ajax({
            type: 'POST',
            processData: false,
            headers:{
        	"X-CSRFToken": csrftoken,
			"X-Requested-With": "XMLHttpRequest"
    		},
    		data : JSON.stringify(datos),
    		dataType: 'json',
            url : 'busca_cp',
            success : function(respuesta) {
                $('#iProvColonia').empty();
                if (respuesta.data_cp.length >0){
                    $('#'+est).val(respuesta.data_cp[0].d_estado);
                    $('#'+ciu).val(respuesta.data_cp[0].d_ciudad);
                    $('#'+mun).val(respuesta.data_cp[0].d_mnpio);
                    for (let i=0 ; i< respuesta.data_cp.length;i++) {
                        $('#iProvColonia').append( '<option value="'+respuesta.data_cp[i].d_asenta+'">'+
                                        respuesta.data_cp[i].d_asenta+'</option>' );
                    }
                    $('#'+call).focus();
                }else{
                    toastr.warning('El código postal no existe...');
                    $('#'+est).val('');
                    $('#'+ciu).val('');
                    $('#'+mun).val('');
                }
                //alert(resultado.data[1].d_estado);

            },
    }).fail( function( jqXHR, textStatus, errorThrown ) {
    	  if (jqXHR.status === 0) {
    		  console.log('No estás conectado, verifica red.');
    	  } else if (jqXHR.status === 404) {
    		  console.log("Página no encontrada [404]...");
    	    //alert('Requested page not found [404]');
    	  } else if (jqXHR.status === 500) {
    		  console.log( 'Interno del Servidor [500].');
    	  } else if (textStatus === 'parsererror') {
    		  console.log('JSON error de parseo.');
    	  } else if (textStatus === 'timeout') {
    		  console.log('Error Time out.');
    	  } else if (textStatus === 'abort') {
    		  alert('Ajax respuesta abortada.');
    	  } else {
    		  console.log( jqXHR.responseText);
    	  }
    	});

}