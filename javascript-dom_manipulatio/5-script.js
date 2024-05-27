document.addEventListener('DOMContentLoaded', () => {
  // Get the element with ID 'update_header'
  const updateHeaderButton = document.querySelector('#update_header');
  // Get the header element
  const header = document.querySelector('header');

  // Add a click event listener to the 'update_header' element
  updateHeaderButton.addEventListener('click', () => {
    // Update the text content of the header element
    header.textContent = 'New Header!!!';
  });
});
