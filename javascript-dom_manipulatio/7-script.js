document.addEventListener('DOMContentLoaded', () => {
  // Get the ul element with id 'list_movies'
  const listMovies = document.getElementById('list_movies');

  // Fetch the movie data from the API
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => {
      // Check if the request was successful
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      // Parse the JSON response
      return response.json();
    })
    .then(data => {
      // Iterate through the array of movie data
      data.results.forEach(movie => {
        // Create a new li element
        const listItem = document.createElement('li');
        // Set the text content of the li element to the movie title
        listItem.textContent = movie.title;
        // Append the li element to the ul list
        listMovies.appendChild(listItem);
      });
    })
    .catch(error => {
      // Log any errors to the console
      console.error('There was a problem with the fetch operation:', error);
    });
});
