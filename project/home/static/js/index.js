$(document).ready(function(){

	Mustache.parse($('#quick_search_get_last_sale').html(),['<%','%>']);
	Mustache.parse($('#quick_search_get_price_composite').html(),['<%','%>']);
	Mustache.parse($('#quick_search_get_daily_open_high_low_close_price').html(),['<%','%>']);
	Mustache.parse($('#quick_search_get_yearly_high_low_price').html(),['<%','%>']);
	Mustache.parse($('#quick_search_get_accrued_interest').html(),['<%','%>']);
	Mustache.parse($('#quick_search_get_bond_calculation').html(),['<%','%>']);
	Mustache.parse($('#quick_search_get_duration_and_convexity').html(),['<%','%>']);
	Mustache.parse($('#broad_range_get_moody_BAA').html(),['<%','%>']);
	// Mustache.parse($('#quick_search_get_last_sale').html(),['<%','%>']);

	// binds click event to a tag by id
	$("#quick_search").on("click", function(event){
		event.preventDefault();
		// var $this = $(this);
		// grabs form template from script tag
		var template = $("#quick_search_template").html();
		// places form on the page
		$("#form-zone").html(template);
	});
	console.log($("#broad_range_search"));
	$("#broad_range_search").on("click", function(event){
		event.preventDefault(); 
		// var $this = $(this);
		var broad_template = $("#broad_range_template").html();
		$("#form-zone").html(broad_template);
	});
	console.log($("#screen_bond_search"));
	$("#screen_bond_search").on("click", function(event){
		event.preventDefault(); 
		// var $this = $(this);
		var screen_template = $("#screen_bond_template").html();
		$("#form-zone").html(screen_template);
	});
	console.log($("#search"));
	$("#search").on("click", function(event){
		event.preventDefault(); 
		// var $this = $(this);
		var search_template = $("#search_template").html();
		$("#form-zone").html(search_template);
	});
	console.log($("#market_search"));
	$("#market_search").on("click", function(event){
		event.preventDefault(); 
		// var $this = $(this);
		var market_search_template = $("#market_search_template").html();
		$("#form-zone").html(market_search_template);
	});
	console.log($("#characteristic_search"));
	$("#characteristic_search").on("click", function(event){
		event.preventDefault(); 
		// var $this = $(this);
		var characteristic_search_template = $("#characteristic_search_template").html();
		$("#form-zone").html(characteristic_search_template);
	});
	$("#form-zone").on("submit", "form#Moodys_Form", function(event){
		event.preventDefault();
		event.stopPropagation();
		var $this = $(this);
		console.log($this.serialize());
		$.ajax({
			method:$this.attr("method"),
			url:$this.attr("action"),
			data:$this.serialize(),
		}).success(function(data){
			// $(".results").html(JSON.stringify(data));
			console.log(data);
			var template = $('#broad_range_'+Object.keys(data)[0]).html();
			console.log(template)
			var rendered = Mustache.render(template, data);

			$(".results").html(rendered);
		}).fail(function(){
			console.log(arguments)
		});
	});
	$("#form-zone").on("submit", "form", function(event){
		event.preventDefault();
		if (this.id==="Moodys_Form") return false;
		var $this = $(this);
		console.log($this.serialize());
		$.ajax({
			method:$this.attr("method"),
			url:$this.attr("action"),
			data:$this.serialize(),
		}).success(function(data){
			// $(".results").html(JSON.stringify(data));
			console.log(data);
			var template = $('#quick_search_'+Object.keys(data)[0]).html();
			console.log(template)
			var rendered = Mustache.render(template, data);

			$(".results").html(rendered);
		}).fail(function(){
			console.log(arguments)
		});
	});
	$("#form-zone").on("submit", "form", function(event){
		event.preventDefault();
		if (this.id==="Moodys_Form") return false;
		var $this = $(this);
		console.log($this.serialize());
		$.ajax({
			method:$this.attr("method"),
			url:$this.attr("action"),
			data:$this.serialize(),
		}).success(function(data){
			// $(".results").html(JSON.stringify(data));
			console.log(data);
			var template = $('#broad_range_'+Object.keys(data)[0]).html();
			console.log(template)
			var rendered = Mustache.render(template, data);

			$(".results").html(rendered);
		}).fail(function(){
			console.log(arguments)
		});
	});
});
console.log("hello");