var map = {
    initialize:function(){
        var timer;
        var blinktime = 500;
        var mapchangetime = 300;
        var    marker_blue=$('#map-marker-main_field-blue');
        var    marker_red=$('#map-marker-main_field-red');
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
        var main_building_click = function(){
            marker_blue=$('#map-marker-main_building-blue');
            marker_red=$('#map-marker-main_building-red');
            $('.map-image-zoomed').animate(
                    {opacity: 0}, 
                    mapchangetime, 
                    function() {
                        $(this).css('background-image','url(\'/media/res/map_front_of_library.png\')').animate({opacity: 1});
                    }
            );
            blink();
        };
        var outdoor_theater_click = function() {
            marker_blue = $("#map-marker-outdoor_theater-blue");
            marker_red = $("#map-marker-outdoor_theater-red");
            $(".map-image-zoomed").animate(
                { opacity: 0 },
                mapchangetime,
                function() {
                    $(this).css("background-image",
                                "url('/media/res/map_outdoor_theater.png')").animate({ opacity: 1});
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
        $("#event-eve_festival").click(function() {
            marker_blue.hide();
            marker_red.show();
            outdoor_theater_click();
            map.update(2);
        });
        $('#event-opening_ceremony').click(function(){
            marker_blue.hide();
            marker_red.show();
            outdoor_theater_click();
            map.update(3);
        });    
        $("#event-badminton").click(function() {
            marker_blue.hide();
            marker_red.show();
            sports_complex_click();
            map.update(4);
        });
        $('#event-basketball').click(function(){
            marker_blue.hide();
            marker_red.show();
            sports_complex_click();
            map.update(5);
        });    
        $("#event-socializing_events").click(function() {
            marker_blue.hide();
            marker_red.show();
            outdoor_theater_click();
            map.update(6);
        });
        $('#event-ai').click(function(){
            marker_blue.hide();
            marker_red.show();
            outdoor_theater_click();
            map.update(7);
        });    
        $('#event-league_of_legends').click(function(){
            marker_blue.hide();
            marker_red.show();
            outdoor_theater_click();
            map.update(8);
        });    
        $("#event-clubs_performances").click(function() {
            marker_blue.hide();
            marker_red.show();
            outdoor_theater_click();
            map.update(9);
        });
        $('#event-baseball').click(function(){ 
            marker_blue.hide();
            marker_red.show();
            sub_field_click();
            map.update(10);
        });
        $('#event-science_quiz').click(function(){
            marker_blue.hide();
            marker_red.show();
            sports_complex_click();
            map.update(11);
        });    
        $('#event-football').click(function(){
            marker_blue.hide();
            marker_red.show();
            main_field_click();
            map.update(12);
        });    
        $('#event-closing_ceremony').click(function(){
            marker_blue.hide();
            marker_red.show();
            outdoor_theater_click();
            map.update(13);
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


