document.addEventListener('DOMContentLoaded', () => {
  // Fetch the character data from the API
  fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => {
      // Check if the request was successful
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      // Parse the JSON response
      return response.json();
    })
    .then(data => {
      // Get the character name from the response data
      const characterName = data.name;
      // Update the text content of the element with id 'character'
      document.getElementById('character').textContent = characterName;
    })
    .catch(error => {
      // Log any errors to the console
      console.error('There was a problem with the fetch operation:', error);
    });
});
