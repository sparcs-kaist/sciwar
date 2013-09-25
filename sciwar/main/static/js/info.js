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
		this.content = $('#content');
	},
	showInfo:function(obj)
	{
		InformationList.content.empty();
		$.each(obj, function(index, item){
			var info = $('<div>', {'class': 'info-field'});

			if (item.classify=="INFO"){
				var classify = $('<div>', {'class': 'info-information'});
				$('<span>').text("INFO").appendTo(classify);
			}
			else{
				var classify = $('<div>', {'class': 'info-notice'});
				$('<span>').text("NOTICE").appendTo(classify);
			}
			classify.appendTo(info);
			$('<div>', {'class': 'info-title'}).text(item.title).appendTo(info);
			$('<div>', {'class': 'info-date'}).text(item.date).appendTo(info);
			$('<div>', {'class': 'info-article'}).text(item.article).appendTo(info);
			info.prependTo(InformationList.content);
		});
	},
};
