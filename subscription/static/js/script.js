var ie = false;
var mobileDevice = false;
var smallDevice = false;
var androidDevice = false;
if(
	navigator.userAgent.match(/Android/i) ||
	navigator.userAgent.match(/webOS/i) ||
	navigator.userAgent.match(/iPhone/i) ||
	navigator.userAgent.match(/iPad/i) ||
	navigator.userAgent.match(/iPod/i))
{
	mobileDevice = true;
}
if ($.browser.msie && $.browser.version < 9) { 
    ie = true;	
	var e = ("article,aside,figcaption,figure,footer,header,hgroup,nav,section,time").split(',');
	for (var i = 0; i < e.length; i++) {
		document.createElement(e[i]);
	}	
}
if (navigator.userAgent.match(/Android/i)) {
	var androidDevice = true;
	$('html').addClass('android');
}
if (navigator.userAgent.match(/iPad/i) || navigator.userAgent.match(/iPod/i)) {
	var smallDevice = true;
	$('html').addClass('smallDevice');
}

$(document).ready(function() {
	
	//Filter
	if ($('.gallery_block').html()) {
		$('.filter_toggler').addClass('toggled');
		$('.header_filter').slideDown();
	}
	
	//Menu SetUp and animation
	$('.menu').find('li:has(ul)').addClass('has-menu');
	$('.menu').children('li.has-menu').addClass('level1');
	$('.menu').find('li.level1').find('ul.sub-menu').children('li.has-menu').addClass('level2');
	$('ul.menu').superfish();
	
	//MobileMenu
	$('.menu').find('li').each(function(){
		cur_link = $(this).children("a");
		if (!$(this).parent('ul').hasClass('sub-menu')) {
			if ($(this).hasClass('current-menu-item')) {
				$('#mobile_select').append('<option selected value="'+cur_link.attr("href")+'">'+cur_link.text().toUpperCase()+'</option>');
			} else {
				$('#mobile_select').append('<option value="'+cur_link.attr("href")+'">'+cur_link.text().toUpperCase()+'</option>');
			}			
		}
		else {
			if ($(this).hasClass('current-menu-item')) {			
				$('#mobile_select').append('<option selected value="'+cur_link.attr("href")+'"> -- '+cur_link.text()+'</option>');
			} else {
				$('#mobile_select').append('<option value="'+cur_link.attr("href")+'"> -- '+cur_link.text()+'</option>');
			}
		}
	});
	
	$('#mobile_select').change(function(){
		select_val = $(this).val();
		window.location = select_val;
	});
	
	//Input and Textarea Click-Clear
	$('input[type=text]').focus(function() {
		if($(this).attr('readonly') || $(this).attr('readonly') == 'readonly') return false;
		if ($(this).val() === $(this).attr('title')) {
				$(this).val('');
		}   
		}).blur(function() {
		if($(this).attr('readonly') || $(this).attr('readonly') == 'readonly') return false;
		if ($(this).val().length === 0) {
			$(this).val($(this).attr('title'));
		}                        
	});	
	$('textarea').focus(function() {
		if ($(this).text() === $(this).attr('title')) {
				$(this).text('');
			}        
		}).blur(function() {
		if ($(this).text().length === 0) {
			$(this).text($(this).attr('title'));
		}                        
	});	
	//FeedBack Form
	$('.content_block').find('.form_field').each(function(){
		$(this).width($(this).parent('form').width()-12);				
	});	
	$('.feedback_go').click(function(){
		var par = $(this).parents(".feedback_form");
		var name = par.find(".field-name").val();
		var email = par.find(".field-email").val();
		var message = par.find(".field-message").val();
		var subject = par.find(".field-subject").val();
		if (email.indexOf('@') < 0) {			
			email = "mail_error";
		}
		if (email.indexOf('.') < 0) {			
			email = "mail_error";
		}
		$.ajax({
			url: "mail.php",
			type: "POST",
			data: { name: name, email: email, message: message, subject: subject },
			success: function(data) {
				$('.ajaxanswer').hide().empty().html(data).show("slow");
		  }
		});
	});
	
	//MapToggler
	
	//Portfolio
	$('.portfolio_content').each(function(){
		$(this).css('margin-top', -($(this).height()/2)+'px');	
	});
	var $container = $('.portfolio_block');
	$('.btn_load_more').click(function() {
		var count = $(this).attr('data-count');
		var $newEls = $(fakeElement.getGroup(count));
		$container.isotope('insert', $newEls, function() {
			//console.log('shyt');
			$container.isotope('reLayout');
			$('.portfolio_content').each(function(){
				$(this).css('margin-top', -($(this).height()/2)+'px');
				$('.prettyPhotoLoaded').prettyPhoto();
			});			
		});
		return false;
	});	
	
	//FilterToggler
	$('.filter_toggler').click(function(){
		$(this).toggleClass('toggled');
		$('.header_filter').slideToggle(400);
	});		
});	

$(window).load(function(){
	/*Landing*/
	if ($('.landing_logo').html()) {
		setTimeout("$('.landing_logo').removeClass('hided')",500);
		setTimeout("$('.landing_enter').removeClass('hided')",1500);
	}
	
	setTimeout("$('#preloader').animate({'opacity' : '0'},300,function(){$('#preloader').hide()})",800);
	setTimeout("$('footer').animate({'opacity' : '1'},500)",800);
	setTimeout("$('.content_wrapper').animate({'opacity' : '1'},500)",800);
	setTimeout("$('.gallery_block').animate({'opacity' : '1'},500)",1000);
	
	footer_setup();
	$('.carouselslider').each(function(){
		dispNum = parseInt($(this).attr('data-count'));
		if ($(window).width()< 485) {
			dispNum = 1;
		}
		$(this).addClass('items'+dispNum);
		$(this).carousel({
			dispItems: dispNum,
			showEmptyItems: 0			
		});				
	});
	if (!mobileDevice) {
		$('.socials').find('a').tipsy({gravity: 's', fade: true});
	}
	//temp form HTML
	$('.accordion').accordion({
		autoHeight: false,
		active: -1,
		collapsible: true
	});
	$('.shortcode_toggles_item_title').click(function(){
		$(this).next().slideToggle();
		$(this).toggleClass('ui-state-active');
	});
	$('.commentlist').find('.stand_comment').each(function(){
		set_width = $(this).width() - $(this).find('.commentava').width() - 25;
		$(this).find('.thiscommentbody').width(set_width);
	});	
	//End Of Temp
	//SideBar Scripts
	if($('aside.sidebar').html()) {
		$('aside.sidebar').find('img').each(function(){
			$(this).wrap('<div class="img_wrapper"></div>')
			$(this).after('<div class="img_fadder" />');
		});
	}
	
	//Portfolio
	$('.prettyPhoto').prettyPhoto();
	
	if ($('.columns1').html()) {
		$('.portfolio_block').isotope('reLayout');
	}
		
	$('.camera_slider_run').each(function(){
		$(this).camera({
			alignment: 'center',
			height: '38.61%',
			fx: 'scrollHorz',
			navigationHover: false,
			loader: 'none' /*pie, bar, none*/,
			mobileNavHover: true,
			time: 4000
		});
		//$(this).cameraStop();		
	});
	
	//Masonry Blog
	$('.masonry_blog_slider').each(function(){
		$(this).camera({
			alignment: 'center',
			height: '50%',
			fx: 'scrollLeft',
			navigationHover: false,
			loader: 'none' /*pie, bar, none*/,
			mobileNavHover: true,
			time: 4000
		});
		//$(this).cameraStop();
	});
	if ($(window).width() > 485) {
		$('.blog-audio').each(function(){
			selector = '#'+$(this).next('.jp-audio').attr('id');
			$(selector).find('.jp-progress').width($(selector).width()-144);
			$('#'+$(this).attr('id')).jPlayer({
				ready: function (event) {
					$('#'+$(this).attr('id')).jPlayer("setMedia", {
						mp3: $(this).attr("data-mp3"),
						oga: $(this).attr("data-ogg")
					});						
				},
				play: function() { // To avoid both jPlayers playing together.
					$('#'+$(this).attr('id')).jPlayer("pauseOthers");
				},					
				swfPath: "js",
				supplied: "mp3, oga",
				cssSelectorAncestor: selector,
				wmode: "window"		
			});
		});		
	}
});
$(window).resize(function(){
	footer_setup();
	$('.blog-audio').find('.jp-progress').width($('.blog-audio').find('.jp-audio').width()-144);
});

function footer_setup() {
	$('.content_wrapper').css('min-height', $(window).height()-$('header').height()-$('footer').height()-$('.header_filter').height()-parseInt($('header').css('border-top-width'))-parseInt($('header').css('border-bottom-width'))+'px');
}
jQuery.fn.TabScroll = function() {
	var scrollStartPos = 0;
	max_scroll = -1*($(this).width()-$('.filter_navigation').width());
	$(this).css('right', max_scroll+'px');
    $(this).bind('touchstart', function(event) {										
        var e = event.originalEvent;
        scrollStartPos = parseInt($(this).css('right')) + e.touches[0].pageX;
    });
    $(this).bind('touchmove', function(event) {										   	
        var e = event.originalEvent;			
        $(this).css('right', (scrollStartPos - e.touches[0].pageX)+'px');
		if (parseInt($(this).css('right')) > 0) {
			$(this).css('right', '0px');
		}
		if (parseInt($(this).css('right')) < max_scroll) {
			$(this).css('right', max_scroll+'px');
		}
        e.preventDefault();
    });
    return this;	
};