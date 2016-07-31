$(document).ready(function () {

  
  var slides = $('.slide');
  var container = $('#slides ul');
  var elm = container.find(':first-child').prop("tagName");
  var item_width = container.width();
  var previous = 'prev'; 
  var next = 'next'; 
  slides.width(item_width);
  container.parent().width(item_width);
  container.width(slides.length * item_width); 
  container.find(elm + ':first').before(container.find(elm + ':last'));
  resetSlides();
  
  
  
  $('#buttons a').click(function (e) {
    
    if (container.is(':animated')) {
      return false;
    }
    if (e.target.id == previous) {
      container.stop().animate({
        'left': 0
      }, 1500, function () {
        container.find(elm + ':first').before(container.find(elm + ':last'));
        resetSlides();
      });
    }
    
    if (e.target.id == next) {
      container.stop().animate({
        'left': item_width * -2
      }, 1500, function () {
        container.find(elm + ':last').after(container.find(elm + ':first'));
        resetSlides();
      });
    }
         
    return false;
    
  });
  
  container.parent().mouseenter(function () {
    clearInterval(run);
  }).mouseleave(function () {
  });
  
  
  function resetSlides() {
    container.css({
      'left': -1 * item_width
    });
  }
  
});


function rotate() {
  $('#next').click();
}

$(document).ready(function () {

  
  var slides = $('.slide2');
  var container = $('#slides2 ul');
  var elm = container.find(':first-child').prop("tagName");
  var item_width = container.width();
  var previous = 'prev2'; 
  var next = 'next2'; 
  slides.width(item_width);
  container.parent().width(item_width);
  container.width(slides.length * item_width); 
  container.find(elm + ':first').before(container.find(elm + ':last'));
  resetSlides();
  
  
  
  $('#buttons2 a').click(function (e) {
    
    if (container.is(':animated')) {
      return false;
    }
    if (e.target.id == previous) {
      container.stop().animate({
        'left': 0
      }, 1500, function () {
        container.find(elm + ':first').before(container.find(elm + ':last'));
        resetSlides();
      });
    }
    
    if (e.target.id == next) {
      container.stop().animate({
        'left': item_width * -2
      }, 1500, function () {
        container.find(elm + ':last').after(container.find(elm + ':first'));
        resetSlides();
      });
    }
         
    return false;
    
  });
  
  container.parent().mouseenter(function () {
    clearInterval(run);
  }).mouseleave(function () {
  });
  
  
  function resetSlides() {
    container.css({
      'left': -1 * item_width
    });
  }
  
});


function rotate() {
  $('#next2').click();
}
