var DayList={
	initialize:function()
	{
		this.update(0);
		this.color(0);
	},
	update:function(num,type)
	{
		var notice = false;
		var i;
		var daytext = $('.day-text');
		var daydetail = $('.day-detail');
		num--;
		for(i=0;;i++)
		{
			if(daytext[i]==null) break;
			if(i==num)
			{
				if(type==0) $(daytext[i]).css("color","#ed462f");
				$(daydetail[i]).css("background","url('/media/res/img_active.png') right 50% no-repeat");
			}
			else
			{
				if(type==0) $(daytext[i]).css("color","#6f7274");
				$(daydetail[i]).css("background","url('/media/res/img_inactive.png') right 50% no-repeat");
			}
		}
		if(num!=-1)
		{
			var str='#frag'+(num);
			$(document.body).animate({
				'scrollTop': $(str).offset().top
			}, 500);
		}
	},
	color:function(num)
	{
		num--;
		var click = $('.day-click');
		var text = $('.day-detail');
		var i;
		for(i=0;;i++)
		{
			if(click[i]==null) break;
			if(i==num)
			{
				$(click[i]).css("background","#ebebeb");
			}
			else
			{
				$(click[i]).css("background","#F5F5F5");
			}
		}
	}
};
