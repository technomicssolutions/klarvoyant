window.addEvent('domready', function(){
	$$('.nephro_div').show();
	$$('.fertility_div').hide();
	$$('.news_div').hide();
	$$('.fertility').addEvent('click', function(e){
		$$('.nephro_div').hide();
		$$('.fertility_div').show();
		$$('.news_div').hide();
	}); 
	$$('.news').addEvent('click', function(e){
		$$('.nephro_div').hide();
		$$('.fertility_div').hide();
		$$('.news_div').show();
	}); 
	$$('.nephro').addEvent('click', function(e){
		$$('.nephro_div').show();
		$$('.fertility_div').hide();
		$$('.news_div').hide();
	});
});