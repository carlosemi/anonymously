$(document).ready(function() {

    //Creating a new post
    $("#post_post").click(function(){
        console.log("clicking post")
        $.ajax({type: "POST",
            url:'add_post/',
            async: false,
            data: {
                paragraph: $("#post_paragraph").val()
            },
            success: function(text){
                console.log("Post Success")
                location.reload()
            }
    
        })
    })

    //Adding a comment to a certain post
    $(".add_comment").click(function(){

        var post_id = $(this).attr("post_id")
        var comment_content = $(`#comment_content_${post_id}`).val()

        console.log("post id= " + post_id)

        $.ajax({type: "POST",
            url:'add_comment/',
            async: false,
            data: {
                post_id: post_id,
                paragraph: comment_content
            },
            success: function(text){
                fetchComments(post_id);
                updateNumComments(post_id);
            }
        })

    })

     // Function to fetch and update comments
    function fetchComments(post_id) {
        $.ajax({
            type: "GET",
            url: 'get_comments/',
            data: {
                post_id: post_id,
            },
            success: function(response){
                console.log(response);
                // Update the comments section here
                // Example: $("#comments_section").html(response);
                $(`#comments_section_${post_id}`).empty();
                // Update the comments section
                response.comments.forEach(function(comment) { 
                    $(`#comments_section_${post_id}`).append(`
                        <li class="comment-item">
                            <div class="d-flex position-relative">
                                <div class="ms-2">
                                    <div class="bg-light rounded-start-top-0 p-3 rounded">
                                        <p class="small mb-0">${comment.paragraph}</p>
                                    </div>
                                    <ul class="nav nav-divider py-2 small">
                                        <li class="nav-item">
                                            <a class="nav-link" href="#!">Likes(${comment.likes})</a>
                                        </li>
                                        <li class="nav-item">
                                            <a class="nav-link" href="#!">Dislikes(${comment.dislikes})</a>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </li>
                    `);
                });
            }
        });
    }

    function updateNumComments(post_id){
        $.ajax({
            type: "GET",
            url: 'get_num_comments/',
            data: {
                post_id: post_id,
            },
            success: function(response){
                console.log(response);
                // Update the comments section here
                // Example: $("#comments_section").html(response);
                $(`#num_comments_id_${post_id}`).empty();
                
                // Update the num comments section
                $(`#num_comments_id_${post_id}`).append(`
                    <i class="bi bi-chat-fill pe-1"></i>Comments (${response.num_comments})
                `);
                
            }
        });
    }
});
