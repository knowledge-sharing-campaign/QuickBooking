function defaultSelection() {
	$('#oneWay').datepicker();
    $('#roundTrip').datepicker();
    $('#roundTrip').css("display", "none");
}

function checkTravelType(option) {
    switch(option.value) {
        case "One Way":
            $('#roundTrip').css("display", "none");
            break;
        case "Round Trip":
            $('#roundTrip').css("display", "inline-block");
            break;
    }
}



