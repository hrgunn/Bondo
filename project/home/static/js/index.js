$(document).ready(function(){
	// binds click event to a tag by id
	$("#quick_search").on("click", function(event){
		event.preventDefault();
		// var $this = $(this);
		// grabs form template from script tag
		var template = $("#quick_search_template").html();
		// places form on the page
		$("#form-zone").html(template);
	});

});
console.log("hello");