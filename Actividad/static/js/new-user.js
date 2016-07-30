$("#pink").click(function(){
    swal({   title: "¡Éxito!",   text: "Estamos creando tu usuario.",   type: "info",  closeOnConfirm: false,   showLoaderOnConfirm: true, }, function(){   setTimeout(function(){     
        swal("¡Tu usuario ha sido creado con exito!");   }, 10000); });
});



// $('.ot-add').submit(function () {
//     $.ajax({
//         'type': 'POST',
//         'url': addOTURL,
//         'data': $(this).serialize(),
//         'success': function (response) {
//             if (response.error) {
//                 console.log(response.error);
//             }
//             checkAvailability();
//             $('.modal').hide();
//             $('body').removeClass('modal-open');
//             $('.modal-backdrop').hide();
//         }
//     });
//     return false;

// });
