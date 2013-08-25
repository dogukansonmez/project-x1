var fakeElement = {};
fakeElement.constanants = 'b c d f g k l m n p q r s t v x z'.split(' ');
fakeElement.vowels = 'a e i o u y'.split(' ');
fakeElement.categories = 'portraits landscapes fashion advertising else'.split(' ');
fakeElement.suffices = 'on ium ogen'.split(' ');
fakeElement.titles = 'Aliquam tempor, Fermentum commodo, Ante Elementum, turpis mauris dapibus, fermentum vel urna, Nulla porttitor faucibus'.split(',');

fakeElement.texts1 = 'Phasellus eu tincidunt quam. Etiam tortor massa, mollis at ultricies eu, blandit eget libero. Phasellus eget dolor diam, at aliquet mi. Donec quis lectus.'.split('..');
fakeElement.texts2 = 'Cursus sodales mattis. Morbi eros augue, viverra nec blandit eget lore vitae vestibul, hendrerit eget nisi.'.split('..');

fakeElement.images = 'img_portfolio1 img_portfolio2 img_portfolio3 img_portfolio4 img_portfolio5 img_portfolio6 img_portfolio7 img_portfolio8 img_portfolio9 img_portfolio10 img_portfolio11 img_portfolio12 img_portfolio13 img_portfolio14 img_portfolio15 img_portfolio16'.split(' ');
fakeElement.getRandom = function(property) {
	var values = fakeElement[property];
	return values[ Math.floor(Math.random() * values.length)];
};
fakeElement.create = function(count) {
	var category = fakeElement.getRandom('categories');
	image = fakeElement.getRandom('images');
	title = fakeElement.getRandom('titles');
	text1 = fakeElement.getRandom('texts1');
	text2 = fakeElement.getRandom('texts2');
	
	category = fakeElement.getRandom('categories');
	className = 'element ' + category;
	
	if (count == '1') {
		return '<div data-category="' + category + '" class="' + category + ' element row"><div class="filter_img"><img src="img/portfolio/'+ image +'.jpg" alt="" width="460" height="297"><div class="portfolio_wrapper"></div><a href="img/portfolio/large/'+ image +'.jpg" class="ico_zoom prettyPhotoLoaded"><span></span></a><a href="portfolio_post.html" class="ico_link"><span></span></a></div><div class="span1-2 portfolio_dscr"><h3>'+ title +'</h3><p>'+ text1 +' <a href="portfolio_post.html">Read more...</a></p></div></div>';
	} else {
		return '<div data-category="' + category + '" class="' + category + ' element row"><div class="filter_img"><img src="img/portfolio/'+ image +'.jpg" alt=""><div class="portfolio_wrapper"></div><div class="portfolio_content"><h5>'+ title +'</h5><p>'+ text1 +'</p><span class="ico_block"><a href="img/portfolio/large/'+ image +'.jpg" class="ico_zoom prettyPhotoLoaded"><span></span></a><a href="portfolio_post.html" class="ico_link"><span></span></a></span></div></div></div>';
	}	
};
fakeElement.getGroup = function(count) {
	var i = Math.ceil(count), newEls = '';
	while (i--) {
		newEls += fakeElement.create(count);
	}
	return newEls;
};

