$(document).ready(function(){
	$("#slider").roundSlider({
	    radius: 120,
	    width: 8,
	    handleSize: "+16",
    	handleShape: "dot",
	    circleShape: "pie",
	    sliderType: "min-range",
	    value: 250,
	    max: "5000",
		readOnly: true,
	    startAngle: 315
	});
	$(".pink-button").click(function(){
		swal({   
		title: "Agregar Código",   
		text: "Escribe el código que buscas redimir:",   
		type: "input",   
		showCancelButton: true,   
		closeOnConfirm: false,   
		animation: "slide-from-top",   
		inputPlaceholder: "1JN3K5H" 
	}, function(inputValue){   
		if (inputValue === false) 
			return false;      
		if (inputValue === "") {     
			swal.showInputError("¡Código No Valido!");     
			return false   }      
			swal("Excelente!", "Tu código: " + inputValue + " es valido.", "success"); 
		});
	});
	
});

