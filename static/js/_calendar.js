let hoy = new Date();
let mes_actual = hoy.getMonth();
let ano_actual = hoy.getFullYear();

let meses =["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"];
let dias = ["Dom","Lun","Mar","Mié","Jue","Vie","Sáb"];
//alert(dias[hoy.getDay()]);
let mesano = document.getElementById("mesano");

muestraCalendar(mes_actual, ano_actual);
muestraHorario();
function muestraCalendar(mes,ano){
	let primerDia = new Date(ano, mes).getDay();
	let diasmes = 32-new Date(ano, mes,32).getDate();
	//alert(primerDia);
	let tabla=document.getElementById("calendario-detalle");
	tabla.innerHTML="";
	mesano.innerHTML=meses[mes]+" "+ano;
	
	let date=1;
	for (let i=0;i<6;i++){
		let ren = document.createElement("tr");
		
		for (let j=0;j<7;j++){
			if (i===0&&j<primerDia){
				let cel=document.createElement("td");
				let celtext = document.createTextNode("");
				cel.appendChild(celtext);
				ren.appendChild(cel);
			}else if(date>diasmes){
					
				break;
			}else{
				let color = "'badge badge-pill badge-primary' style='width:30px;'";
				let citas = "";
				let domingo = new Date(ano, mes, date).getDay();
				if (domingo==0){
					color = "'badge badge-pill badge-danger' style='width:30px;'";
				}
				if (hayCitas(date,mes_actual,ano_actual) && domingo!=0 ){
					let estilo = "style='font-size:10px;text-align:left;'";
					citas = "<button type='button' class='btn btn-primary'>" +
								"Citas <span class='badge badge-light'"+estilo+">9</span>" +
							"</button>";
				}
				
				let cel=document.createElement("td");
				cel.setAttribute('style','text-align :left;');
				cel.innerHTML = "<Button id='"+date+"' onclick='abreAgenda(this.id,mes_actual,ano_actual);' class="+color+">"+date+"</Button>"+
				citas;
								
				//let celtext=document.createTextNode(date);
				//cel.appendChild(celtext);
				ren.appendChild(cel);
				date++;
			}
			
		}
		tabla.appendChild(ren);
	}
}
function previo(){
	ano_actual=(mes_actual===0)? ano_actual-1:ano_actual;
	mes_actual=mes_actual===0? 11: mes_actual-1;
	muestraCalendar(mes_actual, ano_actual);
	
}
function siguiente(){
	ano_actual=mes_actual===11? ano_actual+1:ano_actual;
	mes_actual=(mes_actual+1)%12;
	muestraCalendar(mes_actual, ano_actual);
}
function muestraHorario(){
	let tabla=document.getElementById("lista-detalle");
	
	tabla.innerHTML="";
	//let iniHora = 10:30 ;
	//let finHora = 19:30 ;
	var now = new Date('2018-09-28T10:00:00');
	let mesnum = parseInt(hoy.getMonth()) + 1;
	let cambioColor = true;
	let fecha = ano_actual+"-"+mesnum+"-"+hoy.getDate();
	$('#mesanoLista').html(dias[hoy.getDay()] +" "+hoy.getDate()+" "+ meses[mes_actual+1] +" " + ano_actual);
	var datos = {fecha:fecha}
	$.ajax({
		type: 'POST',    
		processData: false,
        contentType: "application/json",
        dataType : 'json',
        data : JSON.stringify(datos),
        //headers: {"X-CSRF-TOKEN": $("input[name='_csrf']").val()},
        url : '/citas/cargaCita?'+$.param(datos),
        beforeSend: function(resultado) {
        	/*
        	box= bootbox.dialog({ 
        	    message: '<div class="text-center"><i class="fa fa-spin fa-spinner"></i> Cargando ...</div>', 
        	    closeButton: false 
        	});*/
        },
        success : function(resultado) {   
        	M.toast({html:"muestraHorario: "+resultado.mensaje});
        	//alert(resultado);
        	//box.modal('hide');
        }, 
        error: function(objeto, quepaso, otroobj) {
            alert("La búsqueda de la información está tomando demasiado tiempo, la Red podría estar saturada, vuelva a intentarlo en unos segundos.");
        }
        
	});
	
	
	for(var i = 0; i < 19; i++){
		let colorRen ;
		if (cambioColor){
			cambioColor=false;
			colorRen = "#1b667a"
		}	
		else{
			cambioColor=true;
			colorRen = "#0C5195"
		}
		let ren = document.createElement("tr");
		//ren.setAttribute('style','background-color:'+colorRen+';color:#000;height:20px;line-height: 5px;height: 4px;');
		for (let j = 0; j<6;j++){
			let cel=document.createElement("td");
			let celtext = document.createTextNode("");
			switch (j){
				case 0:
					
					celtext = document.createTextNode("");
					cel.appendChild(celtext);
					ren.appendChild(cel);
					cel.innerHTML = "<div class='checkbox'><label><input onclick='citas();' type='checkbox' value=''></label></div>";
					break;
				case 1:
					now.setMinutes(now.getMinutes() + 30);
					celtext = document.createTextNode(now.getHours() + ":" + ("00" + now.getMinutes()).slice(-2));
					cel.appendChild(celtext);
					
					ren.appendChild(cel);
					break;
				case 2: 
					celtext = document.createTextNode("");
					cel.appendChild(celtext);
					ren.appendChild(cel);
					cel.innerHTML = "<label></label>";
					break;
				case 3: 
					celtext = document.createTextNode("");
					cel.appendChild(celtext);
					ren.appendChild(cel);
					cel.innerHTML = "<label></label>";
					break;
				case 4: 
					celtext = document.createTextNode("");
					cel.appendChild(celtext);
					ren.appendChild(cel);
					cel.innerHTML = "<label></label>";
					break;
				case 5: 
					celtext = document.createTextNode("");
					cel.appendChild(celtext);
					ren.appendChild(cel);
					cel.innerHTML = "<label></label>";
					break;
			}
					
		}
		tabla.appendChild(ren);
	    //console.log(now.getHours() + ":" + ("00" + now.getMinutes()).slice(-2));
	}
	
}
function hayCitas(dia,mes,ano){
	return true;
}
function citas(){
	
	$("#citaModal").modal({backdrop: 'static', keyboard: false});
	$('#fechaCita').val();
	//recuperaInfoCliente(nCliente);
	//cargaTablaUsuarios();
	//alert("cargar tablas");
	//initAppConf();
}
function cerrarCita(){
	if (gGuardado==false){
		var r = confirm("Aviso Importante!\nNo haz guardado el registro.\n¿Estás seguro de salir?.");
		  if (r == true) { //salir
			  $('#modalConfiguracionCliente').modal("hide");	
		  } else {
		    alert("Presionaste Cancelar!");
		  }
	}
	else{
		$('#citaModal').modal("hide");	
	}	
	gGuardado=false;
}
function abreAgenda(dia,mes,ano){
	let ajustaMes = mes+1;
	//alert(dia +" "+ ajustaMes +" " + ano );
	$('#fechaCita').html(dia +" "+ ajustaMes +" " + ano);
	$("#citaModal").modal({backdrop: 'static', keyboard: false});
	
}
