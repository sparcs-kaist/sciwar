var SortList = {
	initialize:function()
	{
		this.classify = $('.info-click');
		this.updateInfo("all");
	},
	updateInfo:function(name)
	{
		var notice = false;
		var information = false;
		if(name == "all" || name == "notice")
			notice = true;
		if(name == "all" || name == "information")
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
