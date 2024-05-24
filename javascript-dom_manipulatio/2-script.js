document.addEventListener('DOMContentLoaded', () => {
  // Get the element with ID 'red_header'
  const redHeaderButton = document.querySelector('#red_header');
  // Get the header element
  const header = document.querySelector('header');

  // Add a click event listener to the 'red_header' element
  redHeaderButton.addEventListener('click', () => {
    // Add the class 'red' to the header element
    header.classList.add('red');
  });
});
