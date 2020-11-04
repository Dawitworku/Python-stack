


$('h1').click(function () {
    console.log('You hit me')
})



var dex = document.getElementById('pokedex')
for (var i = 1; i < 10; i++) {

    $.get("https://pokeapi.co/api/v2/pokemon/"+i, function (pokemon) { //parameter is what we are receiving from the api. This fuction is called a callback function. It won't run until i recieve data from the api
        console.log(pokemon)
        console.log(pokemon.sprites.front_default)

        var name = pokemon.name
        var image = pokemon.sprites.front_default
        var poke = document.createElement('h1')
        var mon = document.createElement('img')
        console.log(poke)
        console.log(mon)

        mon.setAttribute('src', image) //creating n attribute and setting the src to be the image
        poke.innerHTML = name.charAt(0).toUpperCase() + name.slice(1)
        //name.toUpperCase()
        dex.appendChild(poke)
        dex.appendChild(mon)
    })
}
