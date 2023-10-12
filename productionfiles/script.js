
$("#add_comment").click(function(){
    $.post('/add_comment',
    {
        paragraph: $("#comment.content").val()
    })

    console.log("Clicked")
})

console.log("Working")