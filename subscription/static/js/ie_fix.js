var e = ("article,aside,figcaption,figure,footer,header,hgroup,nav,section,time").split(',');
for (var i = 0; i < e.length; i++) {
  document.createElement(e[i]);
}
$(window).load(function(){
	$('header').hover(function(){
		$(this).stop().animate({'left' : '0px'}, 600);
		$('.btn_toggle').hide();
	},function(){
		$(this).stop().animate({'left' : '-210px'}, 600);
		$('.btn_toggle').show();
	});
});