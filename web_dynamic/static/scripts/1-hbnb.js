$(document).ready(function() {
	const amenityNames = []
	$('input[type="checkbox"]').change(function() { // select all checkboxes
		const amenityName = $(this).data('name');

		if ($(this).is(':checked')) {
			// store amenity id in variable
			amenityNames.push(amenityName);
		} else {
			// remove amenity id from variable
			const idxToRemove = amenityNames.indexOf(amenityName)
			if (idxToRemove > -1) { // ensure item exists
				amenityNames.splice(idxToRemove, 1) // remove one element
			}
		}

		// update h4 with amenities list checked
		$('#myH4').text(amenityNames.join(', '));
	});
});
