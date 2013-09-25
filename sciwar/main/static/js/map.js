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
			map.update(1);
		});	
		$('#event-beer_party').click(function(){
			marker_blue.hide();
			marker_red.show();
			main_building_click();
			map.update(2);
		});	
		$('#event-soccer').click(function(){
			marker_blue.hide();
			marker_red.show();
			main_field_click();
			map.update(3);
		});	
		$('#event-basketball').click(function(){
			marker_blue.hide();
			marker_red.show();
			sports_complex_click();
			map.update(4);
		});	
        $('#event-baseball').click(function(){
			marker_blue.hide();
			marker_red.show();
			sub_field_click();
			map.update(5);
		});
		$('#event-science_quiz').click(function(){
			marker_blue.hide();
			marker_red.show();
			sports_complex_click();
			map.update(6);
		});	
		$('#event-league_of_legends').click(function(){
			marker_blue.hide();
			marker_red.show();
			sports_complex_click();
			map.update(7);
		});	

		$('#event-ai').click(function(){
			marker_blue.hide();
			marker_red.show();
			sports_complex_click();
			map.update(8);
		});	
		$('#event-closing_ceremony').click(function(){
			marker_blue.hide();
			marker_red.show();
			sports_complex_click();
			map.update(9);
		});
		map.update(0);
		map.color(0);
	},
	update:function(num)
	{
		var i;
		var img = $('.map-click-img');
		num--;
		for(i=0;;i++)
		{
			if(img[i]==null) break;
			if(i==num)
			{
				$(img[i]).css("background", 'url("/media/res/img_active.png") top left no-repeat');
			}
			else
			{
				$(img[i]).css("background", 'url("/media/res/img_inactive.png") top left no-repeat');	
			}	
		}
	},
	color:function(num)
	{
		var i;
		var tab = $('.event-item');
		num--;
		for(i=0;;i++)
		{
			if(tab[i]==null) break;
			if(i==num)
			{
				$(tab[i]).css("background","#ebebeb");
			}
			else
			{
				$(tab[i]).css("background","#F5F5F5");
			}
		}
	}
};


