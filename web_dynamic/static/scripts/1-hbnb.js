document.ready(function () {
	const checkedAmenities = {};
	$("li input[type=checkbox]").change(function () {
		if (this.checked) {
		// Checkbox is checked.. add the amenity ID to the dictionary
			checkedAmenities[this.dataset.name] = this.dataset.id;
		} else {
			// Checkbox is not checked.. remove the amenity ID from the dictionary
			delete checkedAmenities[this.dataset.name];
		}
		$(".amenities h4").text(Object.keys(checkedAmenities).sort().join(", "));
	});
});
