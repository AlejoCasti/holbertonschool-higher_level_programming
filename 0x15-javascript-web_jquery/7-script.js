$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', ({ name }) => {
    $('#character').text(name);
})