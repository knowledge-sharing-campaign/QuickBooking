
$(document).ready(function() {
$('#form').datepicker({ minDate:0});
$('#form2').datepicker({minDate:1});
$('#form2').css("display", "none");
});

function checkTravelType(option) {
        if (option.value !== "Round Trip") {
          $('#form2').css("display", "none");
        } else 
        $('#form2').css("display", "inline-block");

}

// var dateLimit = $('#form').datepicker({ minDate:0});