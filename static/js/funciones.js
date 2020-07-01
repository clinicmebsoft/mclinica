function cargaSelects


function solonumeros(e) {
	var key = window.event ? e.which : e.keyCode;
	if (key < 48 || key > 57)
		e.preventDefault();
}

function isVacio(data) {
    return data.length === 0;
}

function isNumerico(data) {
    return isNaN(data)
}

function isMail(data) {
    var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
    return reg.test(data)
}

function minLongitud(data, lenght) {
    return data.length <= lenght;
}

function maxLongitud(data, lenght) {
    return data.length >= lenght;
}

function isText(data){
	var patt = new RegExp(/^[A-Za-z\u00F1\u00D1\s]+$/g);
	return patt.test(data);
}

function isAlfanumerico(data){
	var patt = new RegExp(/^[A-Z\u00F1\u00D1a-z0-9\s]+$/g);
	return patt.test(data);
}


