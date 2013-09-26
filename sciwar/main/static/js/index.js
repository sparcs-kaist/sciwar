var Info = {
	initialize:function(){
		this.btn_m = $(".live>.map>button");
		this.btn_p = $(".live>.players>button");
		this.map = $(".live>.map>p");
		this.players = $(".live>.players>.players-list");

		this.registerHandlers();
	},
	registerHandlers:function(){
        $(this.btn_m).click(function(){
            if($(this).hasClass("flip-hide")){
                $(Info.map).hide('fast');
                $(this).removeClass("flip-hide").addClass("flip-show");
            }else{
                $(Info.map).show('fast');
                $(this).removeClass("flip-show").addClass("flip-hide");
            }
        });
        $(this.btn_p).click(function(){
            if($(this).hasClass("flip-hide")){
                $(Info.players).hide('fast');
                $(this).removeClass("flip-hide").addClass("flip-show");
            }else{
                $(Info.players).show('fast');
                $(this).removeClass("flip-show").addClass("flip-hide");
            }
        });
	},
};
