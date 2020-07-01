function actualizaAgenda() {
    var initialLocaleCode = 'es';
    var localeSelectorEl = document.getElementById('locale-selector');
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {

      plugins: [ 'interaction', 'dayGrid', 'timeGrid', 'list' ],
      header: {
        left: 'prev ,next today',
        center: 'title',
        right: 'dayGridMonth,timeGridMonth,timeGridDay'
      },
      dateClick: function(info) {

          $("#collapseRegistro").collapse('show');
            $('#iNombre').focus();
            $('#iFecha').val(info.dateStr);
            cargarAulas();
            //alert('clicked ' + info.dateStr);
        },
        events: [
            // my event data
        ],
        eventColor: '#ce1b6a',
        eventTextColor: '#fff',
      locale: initialLocaleCode,
      buttonIcons: false, // show the prev/next text
      weekNumbers: true,
      navLinks: true, // can click day/week names to navigate views
      editable: true,
      eventLimit: true, // allow "more" link when too many events
      events:  citas(),//'http://127.0.0.1:5001/zplai/api/eventos'

    });

    calendar.render();

    // build the locale selector's options
    calendar.getAvailableLocaleCodes().forEach(function(localeCode) {
      var optionEl = document.createElement('option');
      optionEl.value = localeCode;
      optionEl.selected = localeCode == initialLocaleCode;
      optionEl.innerText = localeCode;

    });
    calendar.getEvents()
    //

  }

    // Primer evento
function citas() {
    var listOfEvents = new Array();
    var prom = new Promise(function (resolve, reject) {
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        $.ajax({
              dataType: 'json',
              contentType: "application/json; charset=utf-8",
              type : 'GET',
              headers:{
                "X-CSRFToken": csrftoken,
                "X-Requested-With": "XMLHttpRequest"
                },
             url: 'ax_citas', //eventos pasados no pintarlos 3 días
             async: false,
             success: function (data) {
                 resolve(data)
                 //alert(data.length);
                 for(var i=0; i<data.length; i++) {
                      //for(var i=0;i<10000;i++) {

                          listOfEvents[i] = new Object();
                          listOfEvents[i]["groupId"] = data[i].id;
                          listOfEvents[i]["title"] = data[i].nombre;
                          listOfEvents[i]["start"] = data[i].fecha;
                          //alert(data[i].fecha);
                          //console.log(data[i].nombre);
                     //}
                  }

             },
             error:function (error) {
                toastr.warning(" Error:"+error.toString());
             }

          });
        //alert(e);

    });
    prom.then(data =>{
        //alert(' porm'+data.eventos[0].title);


        //alert("1"+listOfEvents.length);
             //return listOfEvents;
          //resolve(listOfEvents);
    }).catch(err=>{
        console.log('error: '+err);
    })
    //alert(listOfEvents.length);
return listOfEvents;
}

