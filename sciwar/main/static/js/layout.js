var Creators = {
    initialize:function(){
        this.btn_developers = $("#creators>.developers>button");
        this.developers = $("#creators>.developers>.list");
        this.btn_designers = $("#creators>.designers>button");
        this.designers = $("#creators>.designers>.list");
		this.btn_players = $(".live>.players>button");
		this.players = $(".live>.players>.players-table");	

        this.registerHandlers();
    },
    registerHandlers:function(){
        $(this.btn_developers).click(function(){
            if($(this).hasClass("flip-hide")){
                $(Creators.developers).hide('fast');
                $(this).removeClass("flip-hide").addClass("flip-show");
            }else{
                $(Creators.developers).show('fast');
                $(this).removeClass("flip-show").addClass("flip-hide");
            }
        });
        $(this.btn_designers).click(function(){
            if($(this).hasClass("flip-hide")){
                $(Creators.designers).hide('fast');
                $(this).removeClass("flip-hide").addClass("flip-show");
            }else{
                $(Creators.designers).show('fast');
                $(this).removeClass("flip-show").addClass("flip-hide");
            }
        });
        $(this.btn_players).click(function(){
            if($(this).hasClass("flip-hide")){
                $(Creators.players).slideToggle('slow');
                $(this).removeClass("flip-hide").addClass("flip-show");
            }else{
                $(Creators.players).slideToggle('slow');
                $(this).removeClass("flip-show").addClass("flip-hide");
            }
        });
    },
};
