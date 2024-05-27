document.addEventListener('DOMContentLoaded', () => {
  // Get the element with ID 'add_item'
  const addItemButton = document.querySelector('#add_item');
  // Get the <ul> element with class 'my_list'
  const myList = document.querySelector('.my_list');

  // Add a click event listener to the 'add_item' element
  addItemButton.addEventListener('click', () => {
    // Create a new <li> element
    const newItem = document.createElement('li');
    // Set the text content of the new <li> element
    newItem.textContent = 'Item';
    // Append the new <li> element to the <ul> list
    myList.appendChild(newItem);
  });
});
