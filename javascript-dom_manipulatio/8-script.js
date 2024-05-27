document.addEventListener('DOMContentLoaded', () => {
  // Fetch the translation data from the API
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => {
      // Check if the request was successful
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      // Parse the JSON response
      return response.json();
    })
    .then(data => {
      // Get the translation of "hello" from the response data
      const helloTranslation = data.hello;
      // Update the text content of the element with id 'hello'
      document.getElementById('hello').textContent = helloTranslation;
    })
    .catch(error => {
      // Log any errors to the console
      console.error('There was a problem with the fetch operation:', error);
    });
});
