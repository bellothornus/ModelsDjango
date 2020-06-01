$(document).ready(function() {
    $.fn.dataTable.ext.search.push(
        function( settings, data, dataIndex ) {
            //escojo la opcion del usuario y la comparo con el valor de la columna
            var ag_seleccionado = $("select#ag").children("option:selected").text();
            var nivel_area = data[1];
            if (ag_seleccionado==nivel_area){ //para filtrar una parte
                //para depurar
                //alert("Has seleccionado - " + ag_seleccionado + nivel_area);
                return true;
            }
            console.log("Hola");
            return false;
        }
    );
    var table = $('#myTable').DataTable();
    $("select#ag").change(function(){

        //var ag_seleccionada = $(this).children("option:selected").text();
        table
        .search( '' )
        .draw();
        //table.draw();
    });
} );