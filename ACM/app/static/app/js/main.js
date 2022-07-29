
// WebMasters Background Scroll

/* when modal is opened */
document.querySelector(".trigger_popup_fricc",).addEventListener('click', function() {
  document.querySelector(".hover_bkgr_fricc").style.display = 'block';
  document.querySelector("body").style.overflow = 'hidden';
});

/* when modal is closed */
document.querySelector(".popupCloseButton").addEventListener('click', function() {
  document.querySelector(".hover_bkgr_fricc").style.display = 'none';
  document.querySelector("body").style.overflow = 'visible';
});

/////////// Preloader

var preloader = document.getElementById('preloader');

function loadingFunc(){
    preloader.style.display = 'none';
}



                        // sidbarsocial and sidbarevents

$(document).ready(function(){

  $(document).scroll(function(){

    var footerSelector = '.footer';
    var socialBarSelector = '.sidebar';
    var sidebarright = '.sidebarright';

    var bottomViewPort = $(window).scrollTop()+$(window).height();
    var footerTop = $(footerSelector).offset().top;

    if(bottomViewPort>=footerTop){
      $(socialBarSelector).fadeOut();
      $(sidebarright).fadeOut();
    }else{
      $(socialBarSelector).fadeIn();
      $(sidebarright).fadeIn();
    }
  });

});



                      // home page navbar

var $bannerSlider = jQuery('.banner-slider');
var $bannerFirstSlide = $('div.banner-slide:first-child');

$bannerSlider.on('init', function(e, slick) {
  var $firstAnimatingElements = $bannerFirstSlide.find('[data-animation]');
  slideanimate($firstAnimatingElements);
});
$bannerSlider.on('beforeChange', function(e, slick, currentSlide, nextSlide) {
  var $animatingElements = $('div.slick-slide[data-slick-index="' + nextSlide + '"]').find('[data-animation]');
  slideanimate($animatingElements);
});
$bannerSlider.slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  arrows: true,
  fade: true,
  dots: false,
  swipe: true,
  adaptiveHeight: true,
  responsive: [
  {
    breakpoint: 767,
    settings: {
      slidesToShow: 1,
      slidesToScroll: 1,
      autoplay: false,
      autoplaySpeed: 4000,
      swipe: true,
    }
  }
  ]
});
function slideanimate(elements) {
  var animationEndEvents = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
  elements.each(function() {
    var $this = $(this);
    var $animationDelay = $this.data('delay');
    var $animationType = 'animated ' + $this.data('animation');
    $this.css({
      'animation-delay': $animationDelay,
      '-webkit-animation-delay': $animationDelay
    });
    $this.addClass($animationType).one(animationEndEvents, function() {
      $this.removeClass($animationType);
    });
  });
}

// data color
jQuery("[data-color]").each(function () {
jQuery(this).css('color', jQuery(this).attr('data-color'));
});
// data background color
jQuery("[data-bgcolor]").each(function () {
jQuery(this).css('background-color', jQuery(this).attr('data-bgcolor'));
});


$('.owl-banner').owlCarousel({
    items:1,
    loop:true,
    dots: true,
    nav: false,
    autoplay: true,
    margin:0,
      responsive:{
          0:{
              items:1
          },
          600:{
              items:1
          },
          1000:{
              items:1
          },
          1600:{
              items:1
          }
      }
})



                              // roundedcircle

$(document).ready(function(){
  var entries = [
      {label : 'Research'},
      {label : 'Innovation'},
      {label : 'Startups'},
      {label : 'Inspection'},
      {label : 'Exploration'},
      {label : 'Entrepreneurship'},
      {label : 'Modernism'},
      {label : 'Deviation'},
      {label : 'Opportunities'},
      {label : 'Proficiency'},
      {label : 'Excellence'},
      // {label : 'NODE.JS'},
      // {label : 'JAVA'},
      // {label : 'VISUAL BASIC'},
      // {label : 'ACTION SCRIPT'},
      // {label : 'RUBY'},
      // {label : 'OBJECTIVE-C'},
      // {label : 'PASCAL'},
      // {label : 'COBOL'},
      // {label : 'COLD FUSION'},
      // {label : 'PERL'},
      // {label : 'SWITCH APPLE'},
      // {label : 'ALGOL'},
      // {label : 'VISUAL FOXPRO'},
      // {label : 'REBOL'},
  ];

  var settings = {
      entries : entries,
      width:620,
      height:550,
      radius:'70%',
      radiusMin:70,
      bgDraw: true,
      bgColor: 'transparent',
      opacityOver:1.00,
      opacityOut:0.05,
      opacitySpeed:6,
      fov:800,
      speed:0.5,
      fontFamily: 'nunito, sans-serif',
      fontSize:'30',
      fontColor:'#072589',
      fontWeight:'600',
      fontStyle:'normal',
      fontSretch:'normal',      
  };
  $('#tag').svg3DTagCloud(settings);
});


          // counter

  globalmember = $('#number2').text()
  localmember = $('#number3').text()
  events = $('#number4').text()
  

  $.fn.jQuerySimpleCounter = function( options ) {
    var settings = $.extend({
        start:  0,
        end:    100,
        easing: 'swing',
        duration: 400,
        complete: ''
    }, options );
  
    var thisElement = $(this);
  
    $({count: settings.start}).animate({count: settings.end}, {
    duration: settings.duration,
    easing: settings.easing,
    step: function() {
      var mathCount = Math.ceil(this.count);
      thisElement.text(mathCount);
    },
    complete: settings.complete
  });
  }
  
    $('.counterdiv').waypoint({
      handler: function() {
        // $('#number1').jQuerySimpleCounter({end: 12,duration: 3000});
        $('#number2').jQuerySimpleCounter({end: globalmember,duration: 2000});
        $('#number3').jQuerySimpleCounter({end: localmember,duration: 2000});
        $('#number4').jQuerySimpleCounter({end: events,duration: 2500});
  
    },
    offset: '100%'
  });
                            



                              // events


jQuery(document).ready(function($) {

  'use strict';

    $('.imageGallery1 a').simpleLightbox();

    $('.tabgroup > div').hide();
    $('.tabgroup > div:first-of-type').show();
    $('.tabs a').click(function(e){
      e.preventDefault();
        var $this = $(this),
        tabgroup = '#'+$this.parents('.tabs').data('tabgroup'),
        others = $this.closest('li').siblings().children('a'),
        target = $this.attr('href');
    others.removeClass('active');
    $this.addClass('active');
    $(tabgroup).children('div').hide();
    $(target).show();
  
    })
});


(function(factory) {

  if (typeof define === 'function' && define.amd) {
      define(['jquery'], factory);
  } else if (typeof module === 'object' && module.exports) {
      module.exports = factory(require('jquery'));
  } else {
      factory(jQuery);
  }

}(function($) {

  function SimpleLightbox(options) {

      this.init.apply(this, arguments);
  }

  SimpleLightbox.open = function(options) {

      var instance = new SimpleLightbox(options);

      return options.content ? instance.setContent(options.content).show() : instance.showPosition(instance.options.startAt);

  };

  $.fn.simpleLightbox = function(options) {

      var lightboxInstance,
          $items = this;

      return this.each(function() {
          if (!$.data(this, 'simpleLightbox')) {
              lightboxInstance = lightboxInstance || new SimpleLightbox($.extend({}, options, {$items: $items}));
              $.data(this, 'simpleLightbox', lightboxInstance);
          }
      });

  };

  $.simpleLightbox = $.SimpleLightbox = SimpleLightbox;

  return $;

}));




                        ////// About Page


$(document).on("click", ".naccs .menu div", function() {
  var numberIndex = $(this).index();

  if (!$(this).is("active")) {
      $(".naccs .menu div").removeClass("active");
      $(".naccs ul li").removeClass("active");

      $(this).addClass("active");
      $(".naccs ul").find("li:eq(" + numberIndex + ")").addClass("active");

      var listItemHeight = $(".naccs ul")
        .find("li:eq(" + numberIndex + ")")
        .innerHeight();
      $(".naccs ul").height(listItemHeight + "px");
    }
});


$('[data-fancybox="gallery"]').fancybox({
  buttons: [
    "slideShow",
    "thumbs",
    "zoom",
    "fullScreen",
    "download",
    "share",
    "close",
  ],
  loop: false,
  protect: true
});



/////// Local Member

const inputs = document.querySelectorAll(".input");

function focusFunc() {
  let parent = this.parentNode;
  parent.classList.add("focus");
}

function blurFunc() {
  let parent = this.parentNode;
  if (this.value == "") {
    parent.classList.remove("focus");
  }
}

inputs.forEach((input) => {
  input.addEventListener("focus", focusFunc);
  input.addEventListener("blur", blurFunc);
});



                //   Top button arrow


  if($('.bottom_top').length > 0){
    $(function(){
      // Scroll Event
      $(window).on('scroll', function(){
        var scrolled = $(window).scrollTop();
        if (scrolled > 300) $('.bottom_top').addClass('active');
        if (scrolled < 300) $('.bottom_top').removeClass('active');
      });  
      // Click Event
      $('.bottom_top').on('click', function() {
        $("html, body").animate({ scrollTop: "0" },  500);
      });
    });
  }
 


///////////  WebTeam popup  /////////

  $(".trigger_popup_fricc").click(function(){
     $('.hover_bkgr_fricc').show();
  });
  $('.hover_bkgr_fricc').click(function(){
      $('.hover_bkgr_fricc').hide();
  });
  $('.popupCloseButton').click(function(){
      $('.hover_bkgr_fricc').hide();
  });




        ////// Only once times display Event Counter //////////

  function setCookie( c_name, value, exhrs ) {
    var c_value = escape(value);
    if (exhrs) {
      var exdate = new Date();
      exdate.setHours(exdate.getHours() + exhrs)
      // exdate.setDate( exdate.getT() + exdays );
      c_value += '; expires=' + exdate.toUTCString();
    }
    document.cookie = c_name + '=' + c_value;
  }
  
  function getCookie( c_name ) {
    var i, x, y, cookies = document.cookie.split( ';' );
  
    for ( i = 0; i < cookies.length; i++ ) {
      x = cookies[i].substr( 0, cookies[i].indexOf( '=') );
      y = cookies[i].substr( cookies[i].indexOf( '=') + 1 );
      x = x.replace( /^\s+|\s+$/g, '' );
  
      if ( x === c_name ) {
        return unescape( y );
      }
    }
  }

  window.setTimeout(function(){ 
    // When the cookie exists, do not show the popup!
    if (getCookie('displayedPopupNewsletter')) {
      return;
    }
  
    $(document).ready(function() { 
      var id = '#dialog';
      var maskHeight = $(document).height();
      var maskWidth = $(window).width();
      $('#mask').css({'width':maskWidth,'height':maskHeight}); 
      $('#mask').fadeIn(500); 
      $('#mask').fadeTo("slow",0.9); 
            var winH = $(window).height();
      var winW = $(window).width();
            $(id).css('top',  winH/2-$(id).height()/2);
      $(id).css('left', winW/2-$(id).width()/2);
         $(id).fadeIn(2000);  
         $('.window .close').click(function (e) {
      e.preventDefault();
      $('#mask').hide();
      $('.window').hide();
         });  
         $('#mask').click(function () {
      $(this).hide();
      $('.window').hide();
     });  

     // Events Popup Background Scroll

     document.querySelector("#boxes").style.display = 'block';
     document.querySelector("body").style.overflow = 'hidden';
 
     document.querySelector(".close").addEventListener('click', function() {
       document.querySelector("#boxes").style.display = 'none';
       document.querySelector("body").style.overflow = 'visible';
     });
 
     
    });

  
    // The popup was displayed. Set the cookie for 3hr.
    setCookie('displayedPopupNewsletter', 'yes', 3);
  }, 3000);


  // Events Read More......

  $(document).ready(function() {
    var max = 180;
    $(".readMore").each(function() {
        var str = $(this).text();
        if ($.trim(str).length > max) {
            var subStr = str.substring(0, max);
            var hiddenStr = str.substring(max, $.trim(str).length);
            console.log(hiddenStr)
            $(this).empty().html(subStr);
            $(this).append('<a href="javascript:void(0);" class="link"> Read more…</a>');
            $(this).append('<span class="addText">'+hiddenStr+'</span>');
        }
    });
    $(".link").click(function() {
        console.log("hello2")
        $(this).siblings(".addText").contents().unwrap();
        $(this).remove();
    });
  });
  


  
            // Nav background scroll prevent

$('#menu-icon').on('click', function(event){
  // event.preventDefault();
  $('.nav').toggleClass('is-visible');
  if ($('.nav').hasClass("is-visible")) // Changed this line from your link.
    $("body").css("overflow", "hidden");
  else
    $("body").css("overflow", "visible");
});

  

            ///////  Event Counter  ///////////

  var labels = ['Weeks', 'Days', 'Hours', 'Minutes', 'Seconds'],
	TimerCount = (new Date().getFullYear() + 1) + '/01/01',
	template = _.template( jQuery('#main-example-template').html()),
	currDate = '00:00:00:00:00',
	nextDate = '00:00:00:00:00',
	parser = /([0-9]{2})/gi,
	$example = jQuery('#main-example');

	if( $example.data("timer").length ){
		TimerCount = $example.data("timer");	
	}

// Parse countdown string to an object
function strfobj(str) {
	var parsed = str.match(parser),
		obj = {};
	labels.forEach(function(label, i) {
		obj[label] = parsed[i]
	});
	return obj;
}
// Return the time components that diffs
function diff(obj1, obj2) {
	var diff = [];
	labels.forEach(function(key) {
		if (obj1[key] !== obj2[key]) {
			diff.push(key);
		}
	});
	return diff;
}
// Build the layout
var initData = strfobj(currDate);
labels.forEach(function(label, i) {
	$example.append(template({
		curr: initData[label],
		next: initData[label],
		label: label
	}));
});
// Starts the countdown
$example.countdown(TimerCount, function(event) {
	var newDate = event.strftime('%w:%d:%H:%M:%S'),
		data;

	if (newDate !== nextDate) {
		currDate = nextDate;
		nextDate = newDate;
		// Setup the data
		data = {
			'curr': strfobj(currDate),
			'next': strfobj(nextDate)
		};
		// Apply the new values to each node that changed
		diff(data.curr, data.next).forEach(function(label) {
			var selector = '.%s'.replace(/%s/, label),
				$node = $example.find(selector);
			// Update the node
			$node.removeClass('flip');
			$node.find('.curr').text(data.curr[label]);
			$node.find('.next').text(data.next[label]);
			// Wait for a repaint to then flip
			_.delay(function($node) {
				$node.addClass('flip');
			}, 50, $node);
		});
	}
});


