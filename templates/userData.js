function saveFormData() {
  // Get form data
  const form = document.querySelector('form');
  const formData = new FormData(form);
  
  // Create object from form data
  const data = {};
  for (const [key, value] of formData.entries()) {
    data[key] = value;
  }
  
  // Save data to local storage
  const storedData = localStorage.getItem('formData');
  if (storedData) {
    const parsedData = JSON.parse(storedData);
    parsedData.push(data);
    localStorage.setItem('formData', JSON.stringify(parsedData));
  } else {
    localStorage.setItem('formData', JSON.stringify([data]));
  }
}
