var SortList = {
	initialize:function()
	{
		this.updateVideo("all");
	},
	reverseOrder:function()
	{
	},
	updateVideo:function(name)
	{
		$.ajax({
			type: 'GET',
			url: '/video/update/',
			data: {'name':name},
			dataType: 'json',
			success: $.proxy(function(resObj) {
				VideoList.showVideo(resObj.contents);
			}, this),
			error: function(xhr) {
			}
		});
	},
};

var VideoList = {
	initialize:function()
	{
		this.content = $('#content');
	},
	showVideo:function(obj)
	{
		VideoList.content.empty();
		$.each(obj, function(index, item){
			var video = $('<div>', {'class': 'video-item'});
		
			var video_info = $('<div>', {'class': 'video-info'});
			$('<div>', {'class': 'video-title'}).text(item.title).appendTo(video_info);

			var video_event_info = $('<div>', {'class': 'video-eventt-info'});
			$('<div>', {'class': 'video-event'}).text(item.event).appendTo(video_event_info);
			$('<div>', {'class': 'video-time'}).text(item.time).appendTo(video_event_info);
			video_event_info.appendTo(video_info);
			video_info.appendTo(video);

			var video_area = $('<div>', {'class': 'video-area'});
			$('<iframe>', {'width': '420px', 'height': '345px', 'src': "http://www.youtube.com/embed/CM-3W_QXan8"}).appendTo(video_area);
			video_area.appendTo(video);

			var video_link = $('<div>', {'class': 'video-link'});
			$('<a>', {'href': item.link}).text(item.link).appendTo(video_link);
			video_link.appendTo(video);

			video.prependTo(VideoList.content);
		});
	},
};
