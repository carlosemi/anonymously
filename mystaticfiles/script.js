$(document).ready(function() {
    $("#add_comment").click(function(){

        $.ajax({type: "POST",
            url:'add_comment/',
            async: false,
            data: {
                post_id: $("#add_comment").attr("post_id"),
                paragraph: $("#comment_content").val() 
            },
            success: function(text){
                console.log(text)
            }
        })

        $.ajax({ type: "GET",   
         url: "",   
         async: false,
         success : function(text)
         {
             console.log("Success")
         }
        });
    })
});
