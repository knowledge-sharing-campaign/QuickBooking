$(document).ready(function() {
$('#form').datepicker({ minDate:0});
$('#form2').css("display", "none");
});

function checkTravelType(option) {
        if (option.value !== "Round Trip") {
          $('#form2').css("display", "none");
        } else 
        $('#form2').css("display", "inline-block");
}

function oneTripDate(){
	var days = parseInt(($("#form").datepicker("getDate") - new Date())/1000/60/60/24);
	$('#form2').datepicker({minDate: days +2});	
}

function autocompleteFrom(busRoutes){
  loadAutocomplete("#from", busRoutes);
}

function autocompleteTo(busRoutes){
  removeSource(busRoutes);
  loadAutocomplete("#to", busRoutes);
}

function removeSource(busRoutes) {
   var source = document.querySelector("#from").value;
   busRoutes.splice(busRoutes.indexOf(source), 1);
}

function loadAutocomplete (id, busRoutes) {
  $(function() {
    $(id).autocomplete({
      source: busRoutes
    });
  });
}

 function validateForm () {
       return false;
       
 }


        



