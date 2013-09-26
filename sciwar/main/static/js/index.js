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
                $(Info.map).slideUp('fast');
                $(this).removeClass("flip-hide").addClass("flip-show");
            }else{
                $(Info.map).slideDown('fast');
                $(this).removeClass("flip-show").addClass("flip-hide");
            }
        });
        $(this.btn_p).click(function(){
            if($(this).hasClass("flip-hide")){
                $(Info.players).slideUp('fast');
                $(this).removeClass("flip-hide").addClass("flip-show");
            }else{
                $(Info.players).slideDown('fast');
                $(this).removeClass("flip-show").addClass("flip-hide");
            }
        });
	},
};