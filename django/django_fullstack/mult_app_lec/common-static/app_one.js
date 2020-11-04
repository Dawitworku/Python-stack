
$('h1').click(function(){
    console.log('You hit me')
})


$('form').submit(function(event){
    event.preventDefault()
    console.log('Not refreshing the page')

    $.ajax({
        url: '/one/create_user_ajax',
        method: 'post',
        data: $(this).serialize(),
        success: function(response) {
            console.log(response)
            $('#wrestlers').html(response)
        }
    })

    })
    