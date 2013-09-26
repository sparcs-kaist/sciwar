var DayList={
	initialize:function()
	{
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
		if(num!=-1&&type!=0)
		{
			var str='#frag'+(num);
			$(document.body).animate({
				'scrollTop': $(str).offset().top
			}, 500);
		}
	},

};
