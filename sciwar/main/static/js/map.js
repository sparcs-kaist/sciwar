var map = {
	initialize:function(){
		var timer;
		var blinktime = 500;
		var mapchangetime = 300;
		var	marker_blue=$('#map-marker-main_field-blue');
		var	marker_red=$('#map-marker-main_field-red');
		var blink = function(){
			clearTimeout(timer);
			marker_blue.toggle();
			marker_red.toggle();
			timer = setTimeout(blink,blinktime);
		};
		var main_field_click = function(){
			marker_blue=$('#map-marker-main_field-blue');
			marker_red=$('#map-marker-main_field-red');
			$('.map-image-zoomed').animate(
					{opacity: 0}, 
					mapchangetime, 
					function() {
						$(this).css('background-image','url(\'/media/res/map_main_field.png\')').animate({opacity: 1});
					}
			);
			blink();
		};
		var sports_complex_click = function(){
			marker_blue=$('#map-marker-sports_complex-blue');
			marker_red=$('#map-marker-sports_complex-red');
			$('.map-image-zoomed').animate(
					{opacity: 0}, 
					mapchangetime, 
					function() {
						$(this).css('background-image','url(\'/media/res/map_sports_complex.png\')').animate({opacity: 1});
					}
			);
			blink();
		};
		var sub_field_click = function(){
			marker_blue=$('#map-marker-sub_field-blue');
			marker_red=$('#map-marker-sub_field-red');
			$('.map-image-zoomed').animate(
					{opacity: 0}, 
					mapchangetime, 
					function() {
						$(this).css('background-image','url(\'/media/res/map_sub_field.png\')').animate({opacity: 1});
					}
			);
			blink();
		};

		$('#event-soccer').click(function(){
			marker_blue.hide();
			marker_red.show();
			main_field_click();
		});	
		$('#event-baseball').click(function() {
			marker_blue.hide();
			marker_red.show();
			sub_field_click();
		});
		$('#event-science_quiz').click(function() {
			marker_blue.hide();
			marker_red.show();
			sports_complex_click();
		});
	}
}	
