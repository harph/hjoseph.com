$(document).ready(function(){
        
		$('#twitter-area').load('/tweets');
		$('#blog-area').load('/posts');

		$('div.navbar > ul.menu > li > a').click(function(){
			return slideScroll($(this.hash));
		})
});

function slideScroll(target){
        var $target = target;
        $target = $target.length && $target     || $('[name=' + this.hash.slice(1) +']');
        var targetOffset = $target.offset().top - 90;
        $('html,body').animate({scrollTop: targetOffset}, 1000);
        return false;
}
