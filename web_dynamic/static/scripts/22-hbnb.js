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

$(document).ready(function() {
	const url = "http://127.0.0.1:5001/api/v1/status/"
	
	fetch(url)
	  .then(response => {
	      if (response.status == 200) {
	          $('#api_status').addClass('available');
	      } else {
		  $('#api_status').removeClass('available');
	      }
	  })
	  .catch(error => {
	    console.error("Error:", error);
	    $('#api_status').removeClass('available');
	  });
});
