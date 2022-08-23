$(document).on("ready", main);

function main(){
	$("#menu a").on("click", irA);
}

function irA(){
	var seccion = $(this).attr("href");
	$("body, html").animate({
		scrollTop: $(seccion).offset().top-180
	}, 500);
	
	return false;
}