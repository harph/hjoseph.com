$(document).ready(function(){
		$('#twitter-area').load('/tweets');
		$('#blog-area').load('/posts');
		
		$('div.navbar > ul.menu > li > a').click(function(){
			return slideScroll($(this.hash));
		})
		$('div.work-preview > a').fancybox({
			"padding" : "0px", 
			"onComplete" : function(){
				portatolio_preview_loaded();
			},
			"onClosed" : function(){
				portatolio_preview_closed();
			}
		});
});

function slideScroll(target){
        var $target = target;
        $target = $target.length && $target     || $('[name=' + this.hash.slice(1) +']');
        var targetOffset = $target.offset().top - 90;
        $('html,body').animate({scrollTop: targetOffset}, 1000);
        return false;
}


var PORTAFOLIO_INTERVAL = null;

function portatolio_preview_loaded(){
	$(document).ready(function(){
		var imgs = $("div#portafolio-ps > img");
		if(imgs.length > 0){
			$(imgs[0]).fadeIn();
			var cureent_img = 0;
			PORTAFOLIO_INTERVAL = setInterval(function() {
				var old_img = cureent_img;
				if(cureent_img < imgs.length-1){
					cureent_img++;
				}
				else{
					cureent_img = 0;
				}
				$(imgs[cureent_img]).css("z-index", 1);
				$(imgs[old_img]).css("z-index", 2);
				$(imgs[old_img]).fadeOut(1000);
				$(imgs[cureent_img]).fadeIn(200);
			}, 5000);
		}
	});
}

function portatolio_preview_closed(){
	if(PORTAFOLIO_INTERVAL != null){
		clearInterval(PORTAFOLIO_INTERVAL);
		PORTAFOLIO_INTERVAL = null;
	}
}