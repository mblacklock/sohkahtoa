$(document).ready(function() {
		
	$(document).on("click", '#topic-link', function(event){
		event.preventDefault();
		$("#subtopic-list").html(""); // Resets subtopic list
		var year;
	    year = $(this).attr("data-year");
		$.get('/topics/topic_list/', {year: year}, function(data){
			$('#topic-list').html(data);
		});
	});
	
	$(document).on("click", '#subtopic-link', function(event){
		event.preventDefault();
		var topic;
	    topic = $(this).attr("data-topic");
		$.get('/topics/subtopic_list/', {topic: topic}, function(data){
			$('#subtopic-list').html(data);
		});
	});
	
	$('#suggestion').keyup(function(){
		var query;
		query = $(this).val();
		if (query == '') {
			$('#search-list').html('');
		}
		else {
			$.get('/topics/search_list/', {suggestion: query}, function(data){
				$('#search-list').html(data);
			});
		}
	});

});