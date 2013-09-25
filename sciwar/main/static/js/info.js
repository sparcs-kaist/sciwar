var SortList = {
	initialize:function()
	{
		this.classify = $('.info-click');
		this.registerHandles();
		this.updateInfo(this.classify[0]);
	},
	registerHandles:function()
	{
		$.each(this.classify, function(index, item){
			$(item).bind('click', $.proxy(SortList.updateInfo, SortList, item));
		});
	},
	updateInfo:function(obj)
	{
		var notice = false;
		var information = false;
		if(obj.id == "all" || obj.id == "notice")
			notice = true;
		if(obj.id == "all" || obj.id == "information")
			information = true;
		$.ajax({
			type: 'GET',
			url: '/info/update/',
			data: {'notice': notice, 'information': information},
			dataType: 'json',
			success: $.proxy(function(resObj) {
				InformationList.showInfo(resObj.contents);
			}, this),
			error: function(xhr) {
			}
		});
	},
};

var InformationList = {
	initialize:function()
	{
		this.right = $('#right-side');
	},
	showInfo:function(obj)
	{
		console.log(obj);
		InformationList.right.empty();
		$.each(obj, function(index, item){
			var info = $('<div>', {'class': 'info-field'});
		
			var classify = $('<div>', {'class': 'info-classify'}).text(item.classify);
			if (item.classify=="INFO")
				classify.css({"color":"#ffe400"});
			classify.appendTo(info);
			$('<div>', {'class': 'info-title'}).text(item.title).appendTo(info);
			$('<div>', {'class': 'info-date'}).text(item.date).appendTo(info);
			$('<div>', {'class': 'info-article'}).text(item.article).appendTo(info);
			info.prependTo(InformationList.right);
		});
	},
};
