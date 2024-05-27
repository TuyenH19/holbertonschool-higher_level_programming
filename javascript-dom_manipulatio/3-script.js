document.addEventListener('DOMContentLoaded', () => {
  // Get the element with ID 'toggle_header'
  const toggleHeaderButton = document.querySelector('#toggle_header');
  // Get the header element
  const header = document.querySelector('header');

  // Add a click event listener to the 'toggle_header' element
  toggleHeaderButton.addEventListener('click', () => {
    // Toggle the class of the header element between 'red' and 'green'
    if (header.classList.contains('red')) {
      header.classList.remove('red');
      header.classList.add('green');
    } else if (header.classList.contains('green')) {
      header.classList.remove('green');
      header.classList.add('red');
    } else {
      // If the header has neither class, default to 'green'
      header.classList.add('green');
    }
  });
});
