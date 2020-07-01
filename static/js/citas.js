/**
 * https://medium.com/@ninajlu/django-ajax-jquery-search-autocomplete-d4b4bf6494dd
 */

const nombre = document.getElementById('iNombreCitas')
const search = document.getElementById('match-list')
//METER EL AUTOCOMPLETE DE JQUERY
/*
$('#iNombreCitas').on('keyup', function() {
    var words = $(this).val();
    // if input is empty, remove the word count data and return
    if(!words.length) {
        $(this).removeData('wcount');
        return true;
    }
    // if word count data equals the count of the input, return
    if(typeof $(this).data('wcount') !== "undefined" && ($(this).data('wcount') == words.length)){
        return true;
    }
    // update or initialize the word count data
    $(this).data('wcount', words.length);

    console.log('user tiped ' + words);
    // do you stuff...
});
*/

$(document).ready(function () {
	$('#iNombreCitas').autocomplete({
		minlength: 3,
		source: function (req, add) {
			var busca = $('#iNombreCitas').val();
			$.ajax({
				url: '/ajax_BuscaPacientes',
				async: false,
				dataType: 'json',
				type: 'GET',
				data: {'empieza': busca},
				contentType: "application/json",
				success: function (data) {
					//alert(data.respuesta.paciente[0].nombre);
					var sugerencias = [];

					$.each(data.respuesta.paciente, function (index, objeto) {
						var s =data.respuesta.paciente[index].id+'.-'+data.respuesta.paciente[index].nombre+" "+data.respuesta.paciente[index].apellidos
						//alert(s);
						sugerencias.push(s);
					});
					add(sugerencias);
				},
				error: function (err) {
					toastr.info("Error " + err.toString());
				}
			});
		}

	});
	$("#iNombreCitas").change(function () {
		id = $('#iNombreCitas').val()
		//alert(id.lastIndexOf('.-'));
		id = id.substr(0,id.lastIndexOf('.-'));
		obtenDatosPaciente(id);
	});

});
/*
nombres.addEventListener('keypress', (event) => {
  const keyName = event.key;
  //alert('keydown event\n\n' + 'key: ' + keyName);
  if (e.which <= 90 && e.which >= 48 || e.which >= 96 && e.which <= 105)
  {
  	alert('keydown event\n\n' + 'key: ' + keyName);
  }
});
 */

function obtenDatosPaciente(id){
	var csrftoken = $("[name=csrfmiddlewaretoken]").val();
	//alert("hola"+id);
		$.ajax({
			url : '/ajax_obtenDatosPacienteCitas',
			async: false,
			dataType: 'json',
			type: 'GET',
			data: {'id': id},
			contentType: "application/json",
			success : function(data) {
				if (data[0].fields.nombre!=""){
				$('#iNombreCitas').val(data[0].fields.nombre);
				$('#iApellidosCitas').val(data[0].fields.apellidos)
				$('#iCorreoCitas').val(data[0].fields.correo)
				$('#iTelefonoOficinaCitas').val(data[0].fields.telefono)
				$('#iCelularCitas').val(data[0].fields.celular)
				$('#iFechaCita').focus();}
				else{
					toastr.danger('Errror al intentar cargar datos');
				}
				//cerrarCita();
			},
		});
}


function guardaCita(){
		//alert("Guarda cita");
        var nombre = $('#iNombreCitas').val().toUpperCase();
		var apellidos = $("#iApellidosCitas").val().toUpperCase();
		var telefono = $("#iTelefonoOficinaCitas").val();
		if (nombre===""){

			toastr.warning('Falta nombre...');
			$("#iNombreCitas").focus();
			return;
		}
		if (apellidos===""){
			toastr.warning("Faltan apellidos...");
			$("#iApellidosCitas").focus();
			return;
			}
		if (telefono===""){
			toastr.warning("Falta teléfono...");
			$("#iTelefonoOficinaCitas").focus();
			return;
		}
		var correo = $("#iCorreoCitas").val();
		var fecha_cita = $("#iFechaCita").val();
		//alert(fecha_cita);
		var hora = $("#iHoraCitas").val();

		var celular = $("#iCelularCitas").val();
		var motivo = $("#iMotivoCitas").val();

		var datosUsuario = {
				nombre : nombre,
				apellidos: apellidos,
				telefono : telefono,
				correo : correo,
				fecha : fecha_cita,
				hora : hora,
				celular: celular,
				motivo : motivo

				};
		var csrftoken = $("[name=csrfmiddlewaretoken]").val();
		$.ajax({
			type: 'POST',
			processData: false,
			contentType: "application/json",
			dataType : 'json',
			headers:{
        	"X-CSRFToken": csrftoken,
			"X-Requested-With": "XMLHttpRequest"
    		},
			url : '/guardacitas',
			data : JSON.stringify(datosUsuario),
			success : function(resultado) {
				//alert(resultado.respuesta.mensaje);
				if (resultado.respuesta.mensaje.search("existe")>0 ){
				    toastr.warning(resultado.respuesta.mensaje);
				}
				else
				{
				    toastr.success(resultado.respuesta.mensaje);
                }
				limpiaCita();
				//cerrarCita();
			},
		});
}
$(document).on('submit', '#post-form',function(e){
    $.ajax({
        type:'POST',
        url:'{% url "create" %}',
        data:{
            title:$('#title').val(),
            description:$('#description').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        success:function(json){
            document.getElementById("post-form").reset();
            $(".posts").prepend('<div class="col-md-6">'+
                '<div class="row no-gutters border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">' +
                    '<div class="col p-4 d-flex flex-column position-static">' +
                        '<h3 class="mb-0">' + json.title + '</h3>' +
                        '<p class="mb-auto">' + json.description + '</p>' +
                    '</div>' +
                '</div>' +
            '</div>'
            )
        },
        error : function(xhr,errmsg,err) {
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }
    });
});
$
function guardaCitasW(){
	toastr.info("Mensaje de prueba...");
}

function abreCita(){
	$('#modalCita').modal('show');
	//cargaTablaUsuarios();
	$('#modalCita').modal({
	    backdrop: 'static',
	    keyboard: false
	});
	$('#iNombre').focus();
}

function cerrarCita(){	
	$('#modalCita').modal({ dismissible: true});	
	$('#modalCita').modal('handleUpdate');
	$('#modalCita').modal('hide');
}

function limpiaCita(){
	$("#iNombreCitas").val("");
	$("#iApellidosCitas").val("");
	$("#iTelefonoOficinaCitas").val("");
	$("#iCorreoCitas").val("");
	$("#iFechaCita").val("");
	$("#iHoraCitas").val("");
	$("#iHora2").val("");
	$("#iCelularCitas").val("");
	$("#iMotivoCitas").val("");
	$("#iNombreCitas").focus();
}

function guardarCita()
{	

}