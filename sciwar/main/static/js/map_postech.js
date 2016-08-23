var map = {
    initialize:function(){
        var timer;
        var blinktime = 500;
        var mapchangetime = 300;
        var    marker_blue=$('#map-marker-auditorium-blue');
        var    marker_red=$('#map-marker-auditorium-red');
        var blink = function(){
            clearTimeout(timer);
            marker_blue.toggle();
            marker_red.toggle();
            timer = setTimeout(blink,blinktime);
        };
        var auditorium_click = function(){
            marker_blue=$('#map-marker-auditorium-blue');
            marker_red=$('#map-marker-auditorium-red');
            $('.map-image-zoomed').animate(
                    {opacity: 0}, 
                    mapchangetime, 
                    function() {
                        $(this).css('background-image','url(\'/media/res/map_postech_auditorium.png\')').animate({opacity: 1});
                    }
            );
            blink();
        };
        var main_stadium_click = function(){
            marker_blue=$('#map-marker-main_stadium-blue');
            marker_red=$('#map-marker-main_stadium-red');
            $('.map-image-zoomed').animate(
                    {opacity: 0}, 
                    mapchangetime, 
                    function() {
                        $(this).css('background-image','url(\'/media/res/map_postech_main_stadium.png\')').animate({opacity: 1});
                    }
            );
            blink();
        };
        var pocheol_click = function(){
            marker_blue=$('#map-marker-pocheol-blue');
            marker_red=$('#map-marker-pocheol-red');
            $('.map-image-zoomed').animate(
                    {opacity: 0}, 
                    mapchangetime, 
                    function() {
                        $(this).css('background-image','url(\'/media/res/map_postech_pocheol.png\')').animate({opacity: 1});
                    }
            );
            blink();
        };
        var gymnasium_click = function(){
            marker_blue=$('#map-marker-gymnasium-blue');
            marker_red=$('#map-marker-gymnasium-red');
            $('.map-image-zoomed').animate(
                    {opacity: 0}, 
                    mapchangetime, 
                    function() {
                        $(this).css('background-image','url(\'/media/res/map_postech_gymnasium.png\')').animate({opacity: 1});
                    }
            );
            blink();
        };
        var main_stage_click = function() {
            marker_blue = $("#map-marker-main_stage-blue");
            marker_red = $("#map-marker-main_stage-red");
            $(".map-image-zoomed").animate(
                { opacity: 0 },
                mapchangetime,
                function() {
                    $(this).css("background-image",
                                "url('/media/res/map_postech_main_stage.png')").animate({ opacity: 1});
                }
            );
            blink();
        };
        /*
         * Not used in 2015.
        $('#event-beer_party').click(function(){
            marker_blue.hide();
            marker_red.show();
            main_building_click();
            map.update(2);
        });    
        */
        $("#event-hacking_contest").click(function() {
            marker_blue.hide();
            marker_red.show();
            main_building_click(); 
            map.update(1);
        });
        /*
		$("#event-eve_festival").click(function() {
            marker_blue.hide();
            marker_red.show();
            outdoor_theater_click();
            map.update(2);
        });
		*/
        $('#event-opening_ceremony').click(function(){
            marker_blue.hide();
            marker_red.show();
            auditorium_click();
            map.update(2);
        });
        $('#event-football').click(function(){
            marker_blue.hide();
            marker_red.show();
            main_stadium_click();
            map.update(3);
        });    
		/*	
        $("#event-badminton").click(function() {
            marker_blue.hide();
            marker_red.show();
            sports_complex_click();
            map.update(4);
        });
		*/
        $("#event-socializing_events").click(function() {
            marker_blue.hide();
            marker_red.show();
            main_stage_click();
            map.update(4);
        });
        $('#event-ai').click(function(){
            marker_blue.hide();
            marker_red.show();
            main_stage_click();
            map.update(5);
        });    
        $('#event-league_of_legends').click(function(){
            marker_blue.hide();
            marker_red.show();
            main_stage_click();
            map.update(6);
        });    
		/*
        $("#event-clubs_performances").click(function() {
            marker_blue.hide();
            marker_red.show();
            outdoor_theater_click();
            map.update(9);
        });
		*/
        $('#event-baseball').click(function(){ 
            marker_blue.hide();
            marker_red.show();
            pocheol_click();
            map.update(7);
        });
        $('#event-basketball').click(function(){
            marker_blue.hide();
            marker_red.show();
            gymnasium_click();
            map.update(8);
        });    
        $('#event-science_quiz').click(function(){
            marker_blue.hide();
            marker_red.show();
            gymnasium_click();
            map.update(9);
        });    
        $('#event-closing_ceremony').click(function(){
            marker_blue.hide();
            marker_red.show();
            main_stage_click();
            map.update(10);
        });
        map.update(0);
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
};


