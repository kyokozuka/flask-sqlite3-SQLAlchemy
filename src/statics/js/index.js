const url = "http://localhost:5000/todo/add"
$('#addTodo').click(() => {
    const data = {
        name: $('#name').val(),
        description: $('#description').val()
    }
    $.ajax({
        type: 'POST',
        url: url,
        data: data
    })
    .then(d => {
        $('.collapse').toggle()
    })
})
