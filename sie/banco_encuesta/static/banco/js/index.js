$(document).ready(function() {
  $("body").append("<div class='modal'><div class='modal-content'><h4 class='center'>Estadisticas</h4></div></div>");
  $('.modal').modal();

});

function data(id) {
  console.log(id);
  $.ajax({
    url: '/banco/data/'+ id + '/',
    type: 'GET',
    dataType: 'json',
  })
  .done(function(response) {
    var data = response;
    $(".modal-content").html('');
    $(".modal-content").append('<h5 class="center">'+data.nombre+'</h5>')
    .append('<p>'+data.descripcion+'</p>')
    .append('<div class="row"></div>');
    var query = "";
    data.preguntas.forEach(function(element, index){
      $(".modal-content .row").append('<div class="col s12" id="piechart'+index+'" style="height: 500px;"></div>');
      query = "piechart" + index;
      pie(element, query);
    });
    $('.modal').modal('open');
  })
  .fail(function(response) {
    console.log(response);
    alert("Ha ocurrido un error");
  })
  .always(function() {
    console.log("complete");
  });
}

function pie(datos, id){
  google.charts.load('current', {'packages':['corechart']});
  google.charts.setOnLoadCallback(drawChart);

  function drawChart() {
    console.log(datos.respuestas);
    var data = google.visualization.arrayToDataTable(datos.respuestas);

    var options = {
      title: datos.pregunta
    };

    var chart = new google.visualization.PieChart(document.getElementById(id));

    chart.draw(data, options);
  }
}
