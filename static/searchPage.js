const searchButton = document.getElementById('search');
searchButton.addEventListener('click', () => {
    const currURL = window.location.href;
    let nextURL = `${currURL.substring(0, currURL.lastIndexOf('dogs?'))}dogs?`
    if (document.getElementById('breed')['value'] !== 'Any') nextURL += `breed=${document.getElementById('breed')['value']}&`
    if (document.getElementById('age')['value'] !== 'Any') nextURL += `age=${document.getElementById('age')['value']}&`
    if (document.getElementById('size')['value'] !== 'Any') nextURL += `size=${document.getElementById('size')['value']}&`;
    if (document.getElementById('gender')['value'] !== 'Any') nextURL += `gender=${document.getElementById('gender')['value']}&`;
    if (document.getElementById('color')['value'] !== 'Any') nextURL += `color=${document.getElementById('color')['value']}&`;
    window.location.href = nextURL;
});