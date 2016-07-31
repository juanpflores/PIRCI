$(document).ready(function(){
	$("#slider").roundSlider({
	    radius: 120,
	    width: 8,
	    handleSize: "+16",
    	handleShape: "dot",
	    circleShape: "pie",
	    sliderType: "min-range",
	    showTooltip: false,
	    value: 10,
	    readOnly: true,
	    startAngle: 315
	});

});

