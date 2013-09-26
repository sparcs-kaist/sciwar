var Info = {
    initialize:function(){
        this.btn_m = $(".event_detail>.map>button");
        this.btn_p = $(".event_detail>.players>button");
        this.map = $(".event_detail>.map>p");
        this.players = $(".event_detail>.players>.players-list");
        this.goback = $(".event_detail>.go-back");

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
        $(this.goback).click(function(){
            if(parent.history.back() != undefined){
                parent.history.back();
            }else{
                window.close();
            }
        });            
    },
};
