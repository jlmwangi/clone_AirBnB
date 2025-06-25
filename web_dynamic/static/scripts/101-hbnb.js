$(document).ready(function() {
	const amenityNames = []
	$('#amenityCheckbox').change(function() { // select all checkboxes
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

$(document).ready(function() {
	const url = "http://127.0.0.1:5001/api/v1/places_search/"

	const data = {};

	fetch(url, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(data)
	})
	.then(response => {
		if (!response.ok) {
			throw new Error('HTTP error');
		}
		return response.json();
	})
	.then(responseData => {
		//loop through resp data creating an article tag representing a place in section.places
		const section = document.querySelector("section.places");

		responseData.forEach(place => {
			const article = createPlaceArticle(place);
			
			section.appendChild(article);
		});
	})
	.catch(error => {
		console.error("Error fetching places:", error);
	});
});

$(document).ready(function() {
	const amenityNames = []
	const amenityIds = [];
	$('#amenityCheckbox').change(function() { // select all checkboxes
		const amenityName = $(this).data('name');
		const amenityId = $(this).data('id');

		if ($(this).is(':checked')) {
			// store amenity id in variable
			amenityNames.push(amenityName);
			amenityIds.push(amenityId);
		} else {
			// remove amenity id from variable
			const idxToRemove = amenityNames.indexOf(amenityName)
			if (idxToRemove > -1) { // ensure item exists
				amenityNames.splice(idxToRemove, 1); // remove one element
			}
			const idx = amenityIds.indexOf(amenityId)
			if (ids > -1) {
				amenityIds.splice(idx, 1);
			}
		}
	});

	const button = document.querySelector('button');
	button.addEventListener('click', function() {
		const url = "http://127.0.0.1:5001/api/v1/places_search/"

		const requestBody = {
			"states": [],
			"cities": [],
			"amenities": amenityIds
		};

		fetch(url, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(requestBody)
		})
		.then(response => {
			if (!response.ok) {
				throw new Error('HTTP error');
			}
			return response.json();
		})
		.then(responseData => {
			const section = document.querySelector("section.places");

			responseData.forEach(place => {
				const article = createPlaceArticle(place);

				section.appendChild(article);
			});
		})
		.catch(error => {
			console.error("Error fetching places:", error);
		});
	});
});

$(document).ready(function() {
	const stateIds = []
	const cityIds = []
	const amenityIds = []

	$('#stateCheckbox').change(function() { // select all checkboxes
		const stateId = $(this).data('id');

		if ($(this).is(':checked')) {
			// store amenity id in variable
			stateIds.push(stateId);
		} else {
			// remove amenity id from variable
			const idxToRemove = stateIds.indexOf(stateId)
			if (idxToRemove > -1) { // ensure item exists
				stateIds.splice(idxToRemove, 1) // remove one element
			}
		}

		// update h4 with amenities list checked
		$('#myStateId').text(stateIds.join(', '));
	});

	$('#cityCheckbox').change(function() { // select all checkboxes
		const cityId = $(this).data('id');

		if ($(this).is(':checked')) {
			// store amenity id in variable
			cityIds.push(cityId);
		} else {
			// remove amenity id from variable
			const idxToRemove = cityIds.indexOf(cityId)
			if (idxToRemove > -1) { // ensure item exists
				cityIds.splice(idxToRemove, 1) // remove one element
			}
		}

		// update h4 with amenities list checked
		$('#myStateId').text(cityIds.join(', '));
	});

	$('#amenityCheckbox').change(function() { // select all checkboxes
		const amenityName = $(this).data('name');
		const amenityId = $(this).data('id');

		if ($(this).is(':checked')) {
			// store amenity id in variable
			amenityNames.push(amenityName);
			amenityIds.push(amenityId);
		} else {
			// remove amenity id from variable
			const idxToRemove = amenityNames.indexOf(amenityName)
			if (idxToRemove > -1) { // ensure item exists
				amenityNames.splice(idxToRemove, 1); // remove one element
			}
			const idx = amenityIds.indexOf(amenityId)
			if (ids > -1) {
				amenityIds.splice(idx, 1);
			}
		}

		$('#myH4').text(amenityIds.join(', '));
	});

	const button = document.querySelector('button');
	button.addEventListener('click', function() {
		const url = "http://127.0.0.1:5001/api/v1/places_search/"

		const requestBody = {
			"states": stateIds,
			"cities": cityIds,
			"amenities": amenityIds
		};

		fetch(url, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(requestBody)
		})
		.then(response => {
			if (!response.ok) {
				throw new Error('HTTP error');
			}
			return response.json();
		})
		.then(responseData => {
			const section = document.querySelector("section.places");

			responseData.forEach(place => {

				const article = createPlaceArticle(place);

				section.appendChild(article);

			});
		})
		.catch(error => {
			console.error("Error fetching places:", error);
		});
	});
});


$(document).ready(function() {
	$('span').click(function() {
		const span = this;
		const ul = $(this).closest('.reviews').find("ul");


		if ($(span).text() === 'hide') { //text is hide: 
		    ul.empty(); //remove all review elements from dom
		    $(span).text('show');  //change text to show
		}
		else { // text is show
		    const url = "http://127.0.0.1:5000/api/v1/reviews/"

		    fetch(url) //fetch, parse and display reviews: h3 for header and p for review
		      .then(response => {
		          if (!response.ok) {
			      throw new Error('Error fetching review');
			  }
			  return response.json();
		      })
		      .then(data => {
			  //put data into respective h3 and p elements
			  ul.empty();
			  data.forEach(review => {
			    const li = $('<li>');
			    //const h3 = $('<h3>').text(review.title);
		            const p = $('<p>').text(review.text);
			    li.append(p);
			    ul.append(li);
			  });
			  $(span).text('hide');
		      })
		      .catch(error => {
		          console.error('Error fetching review');
		      });
		}
	});
});


function createPlaceArticle(place) {
	const article = document.createElement('article');

	const div1 = document.createElement('div');
	div1.classList.add('price_title');

	const h2 = document.createElement('h2');
	h2.textContent = place.name;

	const div11 = document.createElement('div');
	div11.classList.add('price_by_night');

	const p1 = document.createElement('p');
	p1.innerHTML = place.price_by_night;

	div11.appendChild(p1);
	div1.appendChild(h2);
	div1.appendChild(div11);

	const div2 = document.createElement('div');
	div2.classList.add('information');

	const div21 = document.createElement('div');
	div21.classList.add('max_guest');

	const img1 = document.createElement('img');
	img1.src = 'static/images/icon_group.png';

	const p2 = document.createElement('p');
	p2.innerHTML = `${place.max_guest} Guests`;

	div21.appendChild(img1);
	div21.appendChild(p2);

	const div22 = document.createElement('div');
	div22.classList.add('number_rooms');

	const img2 = document.createElement('img');
	img2.src = 'static/images/icon_bed.png';

	const p3 = document.createElement('p');
	p3.innerHTML = `${place.number_rooms} Rooms`;

	div22.appendChild(img2);
	div22.appendChild(p3);

	const div23 = document.createElement('div');
	div23.classList.add('number_bathrooms');

	const img3 = document.createElement('img');
	img3.src = 'static/images/icon_bath.png';

	const p4 = document.createElement('p');
	p4.innerHTML = `${place.number_bathrooms} Bathooms`;

	div23.appendChild(img3);
	div23.appendChild(p4);

	div2.appendChild(div21);
	div2.appendChild(div22);
	div2.appendChild(div23);

	const div3 = document.createElement('div');
	div3.classList.add('description');

	const p5 = document.createElement('p');
	p5.textContent = place.description;

	div3.appendChild(p5);

	const div4 = document.createElement('div');
	div4.classList.add('reviews');

	const h2 = document.createElement('h2');
	h2.innerHTML = 'Reviews';

	const span = document.createElement('span');
	span.innerHTML = "show";

	h2.appendChild(span);

	const ul = document.createElement('ul');

	div4.appendChild(h2)
	div4.appendChild(ul);

	article.appendChild(div1);
	article.appendChild(div2);
	article.appendChild(div3)
	article.appendChild(div4);

	return article;

}
