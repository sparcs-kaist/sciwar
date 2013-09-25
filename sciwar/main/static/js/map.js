var map = {
	initialize:function(){
		var timer;
		var timeout = 500;
		var	marker_blue=$('#map-marker-main_field-blue');
		var	marker_red=$('#map-marker-main_field-red');
		var blink = function(){
			clearTimeout(timer);
			marker_blue.toggle();
			marker_red.toggle();
			timer = setTimeout(blink,timeout);
		};
		var main_field_click = function(){
			marker_blue=$('#map-marker-main_field-blue');
			marker_red=$('#map-marker-main_field-red');
			blink();
		};
		var sports_complex_click = function(){
			marker_blue=$('#map-marker-sports_complex-blue');
			marker_red=$('#map-marker-sports_complex-red');
			blink();
		};
		var sub_field_click = function(){
			marker_blue=$('#map-marker-sub_field-blue');
			marker_red=$('#map-marker-sub_field-red');
			blink();
		};
                var main_building_click = function(){
			marker_blue=$('#map-marker-main_building-blue');
			marker_red=$('#map-marker-main_building-red');
			blink();
		};



		$('#event-opening_ceremony').click(function(){
			marker_blue.hide();
			marker_red.show();
			sports_complex_click();
		});	
		$('#event-beer_party').click(function(){
			marker_blue.hide();
			marker_red.show();
			main_building_click();
		});	
		$('#event-soccer').click(function(){
			marker_blue.hide();
			marker_red.show();
			main_field_click();
		});	
		$('#event-basketball').click(function(){
			marker_blue.hide();
			marker_red.show();
			sports_complex_click();
		});	
		$('#event-science_quiz').click(function(){
			marker_blue.hide();
			marker_red.show();
			sports_complex_click();
		});	
		$('#event-league_of_legends').click(function(){
			marker_blue.hide();
			marker_red.show();
			sports_complex_click();
		});	

		$('#event-ai').click(function(){
			marker_blue.hide();
			marker_red.show();
			sports_complex_click();
		});	
		$('#event-closing_ceremony').click(function(){
			marker_blue.hide();
			marker_red.show();
			sports_complex_click();
		});
                $('#event-baseball').click(function(){
			marker_blue.hide();
			marker_red.show();
			sub_field_click();
		});	        
	}
	
};


