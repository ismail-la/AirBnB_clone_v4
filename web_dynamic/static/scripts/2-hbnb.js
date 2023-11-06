document.ready(function () {
	const checkedAmenities = {};
	$("li input[type=checkbox]").change(function () {
		if (this.checked) {
			checkedAmenities[this.dataset.name] = this.dataset.id;
		} else {
			delete checkedAmenities[this.dataset.name];
		}
		$(".amenities h4").text(Object.keys(checkedAmenities).sort().join(", "));
	});

	// Retrieve status of API.
	$.getJSON("http://0.0.0.0:5001/api/v1/status/", (data) => {
		if (data.status === "OK") {
			$("div#api_status").addClass("available");
		} else {
			$("div#api_status").removeClass("available");
		}
	});
});
