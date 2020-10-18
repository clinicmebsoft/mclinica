/**
 * 
 */

function EsVacio(campo){
	alert(campo);
	return campo == null || campo === "";
}


let edad = 0;
function tomaValoresFormulario(){
    if (datosPaciente.nombre===""){
		toastr.info("Nombre vacío");
		return
	}
    alert($('#iNombrePaciente').val().toUpperCase());
	datosPaciente = {
		"nombre": $('#iNombrePaciente').val().toUpperCase(),
		"apellidos": $('#iApellidos').val().toUpperCase(),
		"correo" : $('#iCorreoPaciente').val(),
		"fechanacimiento" : $('#iFechaNacimientoPaciente').val(),
		"edad" :  $('#iEdad').val(),
		"sexo":$('#sSexo').val(),
		"ocupacion" : $('#iOcupacion').val(),
		"cp":$('#iCp').val(),
		"telefono":$('#iTelefono').val(),
		"celular":$('#iCelular').val(),
		"calle" : $('#iCalle').val(),
		"colonia":$('#iColonia').val(),
		"comentario" : $('#iComentario').val(),
		"ciudad":$('#iCiudadPaciente').val(),
		"estado":$('#iEstado').val(),
		"pais":$('#iPais').val()
	}
	alert($('#iNombrePaciente').val().toUpperCase());

}

function limpia(){
	  $("#iNombrePaciente").val("");
	  $("#iApellidos").val("");
	  $("#iCorreoPaciente").val("");
	  $("#iFechaNacimientoPaciente").val("");
	  $("#iEdad").val("");
	  $("#sSexo").val("");
	  $("#iOcupacion").val("");
	  $("#iCp").val("");
	  $("#iTelefono").val("");
	  $("#iCelular").val("");
	  $("#iCalle").val("");
	  $("#iColonia").val("");
	  $("#iComentario").val("");
	  $('#iCiudadPaciente').val("");
	  $("#iEstado").val("");
	  $("#iPais").val("");
	  $("#iNombrePaciente").focus();
}

function calculaEdad(){

	var fecha = $('#id_fecha_nacimiento').val();
	var hoy = new Date();
    var cumpleanos = new Date(fecha);
    var edadCal = hoy.getFullYear() - cumpleanos.getFullYear();
    var m = hoy.getMonth() - cumpleanos.getMonth();

    if (m < 0 || (m === 0 && hoy.getDate() < cumpleanos.getDate())) {
        edadCal--;
    }
 
    $('#id_edad').val(edadCal);
    	edad=edadCal;
    return edad;
}

function obtenFoto(){
	//alert(data); 
	var nombreFoto = "hello-world.png";
	 $.ajax({
	        url :"/dameFoto1",             
	          data: {nombreFoto:nombreFoto},
	          type: "GET",
	          contentType: "image/png",
	          
	          dataType: "text",
	        success: function(data) { 
	            //alert(data); 
	              $("#imgalign").html('<img src="' + data + '" />');
	        }
	    });
}

function calculaPorcentaje(){
	var costo = $('#txtCosto').val();
	var descuento = $('#txtDescuento').val();
}


function guardaPacientesValida(){
        alert("hola");
      datosPaciente= {
            "nombre": $('#id_nombre').val().toUpperCase(),
            "apellidos": $('#id_apelidos').val().toUpperCase(),
            "correo": $('#id_correo').val(),
            "fechanacimiento": $('#id_fecha_nacimiento').val(),
            "edad": $('#id_edad').val(),
            "sexo": document.getElementById('id_sexo').value,
            "ocupacion": $('#id_ocupacion').val(),
            "cp": $('#id_cp').val(),
            "telefono": document.getElementById('id_telefono').value,
            "celular": document.getElementById('id_celular').value,
            "calle": $('#id_calle').val(),
            "colonia": $('#id_colonia').val(),
            "comentario": $('#id_observaciones').val(),
            "ciudad": $('#id_ciudad').val(),
            "estado": $('#id_estado').val(),
            "pais": $('#id_pais').val()
        }

    if (datosPaciente.nombre===''){
        toastr.error('Falta nombre de paciente');return }
    if (datosPaciente.apellidos===''){
        toastr.error('Falta apellidos paciente');return }
     if (datosPaciente.correo===''){
        toastr.error('Falta correo ');return }
     if (datosPaciente.fechanacimiento===''){
        toastr.error('Falta fecha nacimiento ');return }
}
function guardaPacientes(){
        datosPaciente= {
           "nombre": $('#id_nombre').val().toUpperCase(),
            "apellidos": $('#id_apelidos').val().toUpperCase(),
            "correo": $('#id_correo').val(),
            "fechanacimiento": $('#id_fecha_nacimiento').val(),
            "edad": $('#id_edad').val(),
            "sexo":  document.getElementById('id_sexo').value,
            "ocupacion": $('#id_ocupacion').val(),
            "cp": $('#id_cp').val(),
            "telefono": $('#id_telefono').val(),
            "celular": $('#id_celular').val(),
            "calle": $('#id_calle').val(),
            "colonia": document.getElementById('id_colonia').value,
            "comentario": document.getElementById('id_observaciones').value,
            "ciudad": $('#id_ciudad').val(),
            "estado": $('#id_estado').val(),
            "pais": $('#id_pais').val()
        }

    if (datosPaciente.nombre===''){
        toastr.error('Falta nombre de paciente');return }
    if (datosPaciente.apellidos===''){
        toastr.error('Falta apellidos paciente');return }
     if (datosPaciente.correo===''){
        toastr.error('Falta correo ');return }
     if (datosPaciente.fechanacimiento===''){
        toastr.error('Falta fecha nacimiento ');return }


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
		async: false,
        data : JSON.stringify(datosPaciente),
        url : '/ajax_guardapaciente',
        beforeSend: function(resultado) {

        },
        success : function(resultado) {
        	//alert(resultado.respuesta.mensaje);
        	//toastr("AVISO", resultado.salida);
        	//alert(resultado.salida);
        	toastr.success(resultado.respuesta.mensaje);
        	if (resultado.respuesta.mensaje.search("Error")<1 ){
        		cargaTpacientes();

        		limpia();
        		location.href='/pacientes/listapacientes';
        		}
        	else{
        	}
        }, 

    	}).fail( function( jqXHR, textStatus, errorThrown ) {
    	  if (jqXHR.status === 0) {
    		  toastr.error('No estás conectado, verifica red.');
    	  } else if (jqXHR.status === 404) {
    	  	toastr.error("Página no encontrada [404]...");
    	    //alert('Requested page not found [404]');
    	  } else if (jqXHR.status === 500) {
    	  	toastr.error('Interno del Servidor [500].');
    	  } else if (textStatus === 'parsererror') {
    		toastr.error('JSON error de parseo.');
    	  } else if (textStatus === 'timeout') {
    		 toastr.error('Error Time out.');
    	  } else if (textStatus === 'abort') {
    		  toastr.error('Ajax respuesta abortada.');
    	  } else {
    		  toastr.error(jqXHR.responseText);
    	  }
    	});
}

function cargaTtratamientos(){
	$(document).ready(function() {
		   var tabla= $('#ttratamientos').DataTable({
			   destroy: true,
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
			    language : {
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
					searchPlaceholder:		"Buscar ",
					zeroRecords:			"No se han encontrado coincidencias.",
					search: 				"Buscar:" ,
		            processing: "Procesando la información",
		            select: {
		                rows: "%d Registros Seleccionados"
		            }
			    },	 
			    "scrollY": "300px",
		        "ajax" : {
					url : "/tratamientos/cargaTtratamientos",
					dataSrc : "reporte",
					type : "GET"
				}
		    } );
		   tabla.on('select', function (e, dt, type, indexes) {
		            var id = dt.row({selected: true}).data()[0];
		     });
		} );
}
function cargaTpacientes(){
	//$('#modalConfiguracionCliente').modal('show');
//$("#modalTablaClientes").modal({backdrop: 'static', keyboard: false});

$(document).ready(function() {
   var tabla= $('#tpacientes').DataTable({
	   destroy: true,
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
	    language : {
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
			searchPlaceholder:		"Buscar ",
			zeroRecords:			"No se han encontrado coincidencias.",
			search: 				"Buscar:" ,
            processing: "Procesando la información",
            select: {
                rows: "%d Registros Seleccionados"
            }
	    },	 
	    "scrollY": "300px",
        "ajax" : {
			url : "ax_CargaTpacientes",
			dataSrc : "data",
			type : "GET"
		},
		columns: [
		    {"data":"id"},
		    {"data":"nombre"},
		    {"data":"apellidos"},
		    {"data":"calle"},
		    {"data":"telefono"},
		    {"data":"celular"},
		    {"data":"correo"}
		]
	   
    } );
   
   $('#tpacientes').on('click','tbody tr',function(){
        let row = tabla.row(this).data();
        editaPAciente(row);
        alert(row['id']);
   })
} );
}
function guardaTratamiento()
{
	var nombreTramiento = $("#txtTratamiento").val();
	var costoTratamiento = $("#txtCosto").val();
	var descuentoTratamiento = $("#txtDescuento").val();
	if (EsVacio(nombreTramiento)){
		 M.toastr({html: 'Falta tratamiento '});
		return
	}
	if (EsVacio(costoTratamiento)){
		 M.toastr({html: 'Falta costo del tratamiento'});
		return
	}
	if (EsVacio(descuentoTratamiento)){
		 M.toastr({html: 'Falta descuento del tratamiento '});
		return
	}
	$.ajax({
		type: 'POST',    
		processData: false,
        contentType: "application/json",
        dataType : 'json',
        url : '/presupuesto/guardarTratamiento',
        data : id,
        success : function(resultado) {  
        	//alert(resultado.salida);
        	
        	 M.toastr({html:resultado.mensaje});
        
        }, 
       
    }).fail( function( jqXHR, textStatus, errorThrown ) {
    	  if (jqXHR.status === 0) {
    		  M.toastr({html:'No estás conectado, verifica red.'});
    	  } else if (jqXHR.status === 404) {
    		  M.toastr({html:'Página no encontrada [404]...'});
    	    //alert('Requested page not found [404]');
    	  } else if (jqXHR.status === 500) {
    		  M.toastr({html:'Interno del Servidor [500].'});
    	  } else if (textStatus === 'parsererror') {
    		  M.toastr({html:'JSON error de parseo.'});
    	  } else if (textStatus === 'timeout') {
    		  M.toastr({html:'Error Time out.'});
    	  } else if (textStatus === 'abort') {
    		  M.toastr({html:'Ajax respuesta abortada.'});
    	  } else {
    		  M.toastr({html:jqXHR.responseText});
    	  }
    	});
}

function muestraFormCliente(id){
	$.ajax({
		type: 'POST',    
		processData: false,
        contentType: "application/json",
        dataType : 'json',
        //headers: {"X-CSRF-TOKEN": $("input[name='_csrf']").val()},
        url : '/clientes/consulta',
        data : id,
        success : function(resultado) {  
        	//alert(resultado.salida);
        	MensajeSalida("Seleccionó número de cliente: "+resultado[0].numcliente);

        	if (resultado[0].numcliente===id){
        		$("#iNumCliente").val(resultado[0].numcliente);
        		nombre.val(resultado[0].nombre);
        		apellidos.val(resultado[0].apellidos);
        		calle.val(resultado[0].calle);
        		colonia.val(resultado[0].colonia);
        		num.val(resultado[0].numero);
        		ciudad.val(resultado[0].ciudad);
        		estado.val(resultado[0].estado);
        		pais.val(resultado[0].pais);
        		cp.val(resultado[0].cp);
        		telefono.val(resultado[0].telefono);
        		correo.val(resultado[0].correo);
        	}
        	else{
        		alert("Error el id no coincide...");
        	}
        },
    }).fail( function( jqXHR, textStatus, errorThrown ) {
    	  if (jqXHR.status === 0) {
    		  alert('No estás conectado, verifica red.');
    	  } else if (jqXHR.status === 404) {
    		  alert("Página no encontrada [404]...");
    	    //alert('Requested page not found [404]');
    	  } else if (jqXHR.status === 500) {
    		  alert( 'Interno del Servidor [500].');
    	  } else if (textStatus === 'parsererror') {
    		  alert('JSON error de parseo.');
    	  } else if (textStatus === 'timeout') {
    		  alert('Error Time out.');
    	  } else if (textStatus === 'abort') {
    		  alert('Ajax respuesta abortada.');
    	  } else {
    		  alert( jqXHR.responseText);
    	  }
    	});
}
function abreModalTratamiento(){
	//cargaTablaUsuarios();
	$('#modalTratamiento').modal('open');
		document.getElementById("txtTratamiento").focus();
	$("#modalTratamiento").modal({
	    dismissible: false
	  });
	$('#txtTratamiento').focus();
}
function cerrarModalTratamiento(){
	$('#modalTratamiento').modal({ dismissible: true});	
	$('#modalTratamiento').modal('handleUpdate');
	$('#modalTratamiento').modal('hide')
}
function abreNuevoPaciente(){
	$('#modalPacienteNuevo').modal('show');
	//cargaTablaUsuarios();
	$('#modalPacienteNuevo').modal({
	    backdrop: 'static',
	    keyboard: false
	});
	$('#iNombre').focus();
}
function cerrarNuevoPaciente(){
	$('#modalPacienteNuevo').modal({ dismissible: true});	
	$('#modalPacienteNuevo').modal('handleUpdate');
	$('#modalPacienteNuevo').modal('hide');
}

function initHP(){
	//alert("Hola");
	var numPaciente = dameNP();
	
}
function dameNP(){
	$.ajax({
		type: 'GET',    
        headers: {"X-CSRF-TOKEN": $("input[name='_csrf']").val()},
        url : '/DNC',
        data : {usu:""},
        success : function(resultado) {  
        	alert(resultado.mensaje);
        },
    }).fail( function( jqXHR, textStatus, errorThrown ) {
    	  if (jqXHR.status === 0) {
    		  toastr("Error",'No estás conectado, verifica red.');
    	  } else if (jqXHR.status === 404) {
    		  toastr("Error","Página no encontrada [404]...");
    	    //alert('Requested page not found [404]');
    	  } else if (jqXHR.status === 500) {
    	    alert('Error Interno del Servidor [500].')
    	  } else if (textStatus === 'parsererror') {
    	    alert('JSON error de parseo.');
    	  } else if (textStatus === 'timeout') {
    	    alert('Error Time out.');
    	  } else if (textStatus === 'abort') {
    	    alert('Ajax respuesta abortada.');
    	  } else {
    	    alert('Error: ' + jqXHR.responseText);
    	  }
    	});
}

function registroPacientesHC(){
	//alert('hola');
	//launch_toastr("info","Mensaje de prueba...").val();
	var numeroPaciente = $("#iNumeroPaciente").val();
	var nombre = $("#iNombre").val();
	var apellidos = $("#iApellidos").val();
	var correo=$("#iCorreoPaciente").val();
	var fechaNacimiento = $("iFechaNacimiento").val();
	var edad = $("#iEdad").val();
	var sexo = $("#iSexo").val();
	var ocupacion = $("#iOcupacion").val();
	var cp = $("#iCp").val();
	var horaCita = $("#iHoraCita").val();
	var telefono = $("#iTelefono").val();
	var celular = $("#iCelular").val();
	var comentarios = $("#iComentarios").val();
	if (numerocliente === ""){
		toas("info","Falta número de cliente...");
		$("#iNumeroCliente").focus();
		return;
	}
	if (nombre === ""){
		toas("info","Falta nombre...");
		$("iNombre").focus();
		return;
	}
	if (apellidos === ""){
		toas("info","Faltan apellidos...");
		$("iApellidos").focus();
		return;
	}
	var datos  = {
		numeroCliente : numeroCliente,
		nombre : nombre,
		apellidos : apellidos,
		correo : correo,
		fecha_Nacimiento : fechaNacimiento,
		edad : edad,
		sexo : sexo,
		ocupacion : ocupacion,
		cp : cp,
		hora_Cita : horaCita			
	}
	$.ajax({
		type: 'POST',    
		processData: false,
        contentType: "application/json",
        dataType : 'json',
        headers: {"X-CSRF-TOKEN": $("input[name='_csrf']").val()},
        url : '/pacientes/guardarHistoria',
        data : JSON.stringify(datos),
        success : function(resultado) {  
        	//alert(resultado.mensaje);
        	limpiaCita();
        	cerrarCita();
        }, 
       
    }).fail( function( jqXHR, textStatus, errorThrown ) {
    	  if (jqXHR.status === 0) {
    		  toastr("Error",'No estás conectado, verifica red.');
    	  } else if (jqXHR.status === 404) {
    		  toastr("Error","Página no encontrada [404]...");
    	    //alert('Requested page not found [404]');
    	  } else if (jqXHR.status === 500) {
    	    alert('Error Interno del Servidor [500].');
    	  } else if (textStatus === 'parsererror') {
    	    alert('JSON error de parseo.');
    	  } else if (textStatus === 'timeout') {
    	    alert('Error Time out.');
    	  } else if (textStatus === 'abort') {
    	    alert('Ajax respuesta abortada.');
    	  } else {
    	    alert('Error: ' + jqXHR.responseText);
    	  }
    	});	
}


function CargaHC(id){
    alert('Cargando historia clínica' + id);
}

function guardaHistoria(id){
    //alert("Guarda Historia");
    const origin = $('#iOriginario').val();
    const medi = $('#iMedico').val();
    const telmed = $('#iTelefonoMedico').val();
    const cirugia  = $('#iCirugia').val();


    const higi = document.querySelectorAll('input[name="iHigiene"]');
    let higiene='';
    for (const h of higi) {
        if (h.checked) {
            higiene = h.value;
            break;
        }
    }
    const alimen = document.querySelectorAll('input[name="iAlimentacion"]');
    let alimentacion='';
    for (const a of alimen) {
        if (a.checked) {
            alimentacion = a.value;
            break;
        }
    }
    let dolorarticula = false;
    const dolora = document.getElementById('cDolorArticulacion').value;
    if (dolora=='on') {
        dolorarticula = true;
    }
    let chasquido = false;
    const chas = document.getElementById('cChasquidosRuidos').value;
    if (chasquido=='on'){
        chasquido = true;
    }
   let limiteapertura = false;
    const lim = document.getElementById('cLimitacionApertura').value;
    if (lim=='on'){
        limiteapertura = true;
    }
    let limitemovi = false;
    const limm = document.getElementById('cLimitacionMovimientos').value;
    if (limm=='on'){
        limitemovi = true;
    }
    let bruxismo = false;
    const bru = document.getElementById('cBruxismo').value;
    if (bru=='on'){
        bruxismo = true;
    }

    //alert(dolorarticula);


    //alert($('#EnfermedadGrave').val());
    datos = {
        id : id,
        origin : origin,
        medi : medi,
        telmed : telmed,
        cirugia : cirugia,
        motivo : $('#iMotivo').val(),
        enfermedadUiltimosA : $('#iEnfermedadUltimosAnos').val(),
        EnfermedadGrave : $('#iEnfermedadGrave').val(),
        Cirugia : $('#iCirugia').val(),
        TraumatismoSecuelas : $('#iTraumatismoSecuelas').val(),
        Transfusiones : $('#iTransfusiones').val(),
        Hemorragias : $('#iHemorragias').val(),
        DonadorSangre : $('#iDonadorSangre').val(),
        AccidenteTratamientos : $('#iAccidenteTratamientos').val(),
        TomaMedicamento : $('#iTomaMedicamento').val(),
        Enfermedades : $('#iEnfermedades').val(),
        Familiar : $('#iFamiliar').val(),
         AlguienEnfermo    : $('#iAlguienEnfermo').val(),
         Embarazada        : $('#iEmbarazada').val(),
         Higiene           : higiene,
         CepilladosDia     : $('#iCepilladosDia').val(),
         Alimentacion      : alimentacion,
         Integrantes       : $('#iIntegrantes').val(),
         Deporte           : $('#iDeporte').val(),
         Habito            : $('#iHabito').val(),
         Temperatura       : $('#iTemperatura').val(),
         Presion           : $('#iPresion').val(),
         Pulso                        : $('#iPulso').val(),
         TratamientoReciente          : $('#iTratamientoReciente').val(),
         Alergico                     : $('#iAlergico').val(),
         Experiencia                  : $('#iExperiencia').val(),
         ArticulacionTemporoMandibular: $('#iArticulacionTemporoMandibular').val(),
         DolorArticulacion            : dolorarticula,
         ChasquidosRuidos             : chasquido,
         LimitacionApertura           : limiteapertura,
         LimitacionMovimientos        : limitemovi,
         Bruxismo                     : bruxismo,

         Observaciones                : $('#tObservaciones').val(),

    }
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
        url : '/pacientes/ajx_guarda_historia',
        data : JSON.stringify(datos),
        success : function(resultado) {
        	//alert(resultado.respuesta.mensaje);
             if (resultado.respuesta.mensaje.includes('Error')){
                 toastr.error(resultado.respuesta.mensaje);
             }else {
                 toastr.success(resultado.respuesta.mensaje);
             }
        },

    }).fail( function( jqXHR, textStatus, errorThrown ) {
    	  if (jqXHR.status === 0) {
    		  toastr.error({html:'No estás conectado, verifica red.'});
    	  } else if (jqXHR.status === 404) {
    		  toastr.error({html:'Página no encontrada [404]...'});
    	    //alert('Requested page not found [404]');
    	  } else if (jqXHR.status === 500) {
    		  toastr.error({html:'Interno del Servidor [500].'});
    	  } else if (textStatus === 'parsererror') {
    		  toastr.error({html:'JSON error de parseo.'});
    	  } else if (textStatus === 'timeout') {
    		  toastr.error({html:'Error Time out.'});
    	  } else if (textStatus === 'abort') {
    		  toastr.error({html:'Ajax respuesta abortada.'});
    	  }
    	});

}
