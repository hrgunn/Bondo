var drawGraph = function draw_graph (dataset){
	console.log(dataset);
	var chart = c3.generate({
		bindto: '.results',
	    data: {
	    	x:'Dates',
	    	xFormat: '%Y-%m-%d',
	    	columns: [
	        	dataset.dates,
	        	dataset.data
	        ],
		    color: {
	        	pattern: ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c', '#98df8a', '#d62728', '#ff9896', '#9467bd', '#c5b0d5', '#8c564b', '#c49c94', '#e377c2', '#f7b6d2', '#7f7f7f', '#c7c7c7', '#bcbd22', '#dbdb8d', '#17becf', '#9edae5']
	    	}
	    

	    },

	    axis: {
	        x: {
	            type: 'timeseries',
	            tick: {
	                format: '%Y-%m-%d'
	                // format: d3.timeFormat("%x")
	            }
	        }
	    }
	});
};

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
		console.log($this.attr("method"));
		$.ajax({
			method:$this.attr("method"),
			url:$this.attr("action"),
			data:$this.serialize(),
		}).success(function(data){
			// $(".results").html(JSON.stringify(data));
			// var template = $('#broad_range_'+Object.keys(data)[0]).html();
			// console.log(template)
			// var rendered = Mustache.render(template, data);
			var moodys_dataset = data.get_moody.dataset_data.data
			var date_range = moodys_dataset.map(function(element, index){
				return element[0];
			});
			date_range.unshift('Dates');
			var moodys = moodys_dataset.map(function(element, index){
				// console.log(element);
				return element[1];
				// return {date:element[0], value:element[1]};
			});
			moodys.unshift('Moody');
			var template = $('#broad_range_'+Object.keys(data)[0]).html();
			console.log(template)
			var rendered = Mustache.render(template, data);

			$(".results").html(rendered);
			drawGraph({dates: date_range, data:moodys});

			var merrill_dataset = data.get_merrill.dataset_data.data
			var merrill = merrill_dataset.map(function(element, index){
				return {date:element[0], value:element[1]};
			});
			$(".results").html(rendered);
			drawGraph({dates: date_range, data:moodys});
			console.log(merrill);
			console.log(moodys);
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