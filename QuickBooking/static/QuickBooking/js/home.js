
$(document).ready(function() {
$('#form').datepicker();
$('#form2').datepicker();
$('#form2').css("display", "none");
});

function checkTravelType(option) {
        if (option.value !== "Round Trip") {
          $('#form2').css("display", "none");
        } else 
        $('#form2').css("display", "inline-block");

}
