var Info = {
	initialize:function(){
		this.btn_m = $(".live>.map>button");
		this.btn_p = $(".live>.players>button");

		this.registerHandlers();
	},
	registerHandlers:function(){
        $(this.btn_m).click(function(){
            if($(this).hasClass("flip-hide")){
				$(this).parents('.live').find('.map>p').slideUp('fast');
                $(this).removeClass("flip-hide").addClass("flip-show");
            }else{
				$(this).parents('.live').find('.map>p').slideDown('fast');
                $(this).removeClass("flip-show").addClass("flip-hide");
            }
        });
        $(this.btn_p).click(function(){
            if($(this).hasClass("flip-hide")){
				$(this).parents('.live').find('.players-list').slideUp('fast');
                $(this).removeClass("flip-hide").addClass("flip-show");
            }else{
				$(this).parents('.live').find('.players-list').slideDown('fast');
                $(this).removeClass("flip-show").addClass("flip-hide");
            }
        });
	},
};
