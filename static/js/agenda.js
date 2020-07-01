/**
 * 
 */

$(document).ready(function() {
  //Autocomplete
  $(function() {
    $.ajax({
      type: 'GET',
      url: '/pacientes/listaPacientes',
      success: function(response) {
        var pacientesArray = response;
        var dataPacientes = {};
        for (var i = 0; i < pacientesArray.length; i++) {
          //console.log(countryArray[i].name);
          dataPacientes[pacientesArray[i].nombre+","+pacientesArray[i].apellidos] = pacientesArray[i].flag; //countryArray[i].flag or null
        }
        $('input.autocomplete').autocomplete({
          data: dataPacientes,
          limit: 5, // The max amount of results that can be shown at once. Default: Infinity.
        });
      }
    });
  });
});