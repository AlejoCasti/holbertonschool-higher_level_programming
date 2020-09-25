$.get('https://swapi-api.hbtn.io/api/films/?format=json', ({results}) => {
    results.map(({title}) => {
        $('#list_movies').append(`<li>${title}</li>`)
    });
})