var SortList = {
	initialize:function()
	{
		this.name="all";
		this.ordering = 0;
		this.updateVideo("all",0);
	},
	reverseOrder:function()
	{
		this.ordering = 1 - this.ordering;
		$.ajax({
			type: 'GET',
			url: '/video/update/',
			data: {'name':this.name, 'order':this.ordering},
			dataType: 'json',
			success: $.proxy(function(resObj) {
				/* TODO: change arrow pointer */
			//	$('.video-click-img-active').toggleClass("video-click-img-active video-click-img");
			//	$($('.video-click-img')[id]).toggleClass("video-click-img video-click-img-active");
				if(this.ordering == 1)
					$('.video-click-order').css("background","url('/media/res/img_up.png') right 50% no-repeat");
				else
					$('.video-click-order').css("background","url('/media/res/img_down.png') right 50% no-repeat");
				VideoList.showVideo(resObj.contents);
			}, this),
			error: function(xhr) {
			}
		});
	},
	updateVideo:function(name,id)
	{
		this.name = name
		$.ajax({
			type: 'GET',
			url: '/video/update/',
			data: {'name':name, 'order':this.ordering},
			dataType: 'json',
			success: $.proxy(function(resObj) {
				/* TODO: change arrow pointer */
				$('.video-click-img-active').toggleClass("video-click-img-active video-click-img");
				$($('.video-click-img')[id]).toggleClass("video-click-img video-click-img-active");

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

			var video_event_info = $('<div>', {'class': 'video-event-info'});
			$('<div>', {'class': 'video-event'}).text(item.event).appendTo(video_event_info);
			$('<div>', {'class': 'video-time'}).text(item.time).appendTo(video_event_info);
			video_event_info.appendTo(video_info);
			video_info.appendTo(video);

			/*
			var new_link = "http://www.youtube.com/v/" + item.link.split("v=")[1];
			var video_area = $('<div>', {'class': 'video-area'});
			$('<embed>', {'width': '630px', 'height': '360px', 'type': 'application/x-shockwave-flash', 'src': new_link}).appendTo(video_area);
			video_area.appendTo(video);
			*/

			var new_link = "http://www.youtube.com/embed/" + item.link.split("v=")[1];
			var video_area = $('<div>', {'class': 'video-area'});
			$('<iframe>', {'width': '630px', 'height': '360px', 'frameborder': '0', 'src': new_link}).appendTo(video_area);
			video_area.appendTo(video);

			video.appendTo(VideoList.content);
		});
	},
};
