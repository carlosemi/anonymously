$(document).ready(function() {

    const sessionID = getCookie('session_id');

    if (sessionID === undefined) {
        $.get('/home/get_session_id/', function(data) {
            console.log(data.session_id)
            setCookie('session_id', data.session_id, 1); // Set the session ID cookie for 1 day
        });
    }


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
                $(`#comment_content_${post_id}`).val('')
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
                                            <a class="nav-link like_comment" id="like_comment_${post_id}_${comment.id}" post_id="${post_id}" comment_id="${comment.id}" >Likes(${comment.num_likes})</a>
                                        </li>
                                        <!-- 
                                        <li class="nav-item">
                                             <a class="nav-link" href="#!">Dislikes(${comment.dislikes})</a>
                                         </li>
                                         -->
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

    //Like a post
    $(".like_post").click(function(){

        var post_id = $(this).attr("post_id")

        $.ajax({type: "POST",
            url:'like_post/',
            async: false,
            data: {
                post_id: post_id,
                session_id: sessionID
            },
            success: function(response){
                console.log(response)

                if(response == "False"){
                    console.log("Post is liked by you already") 
                    return 
                }

                var post_likes = response.post_likes

                console.log("Post likes = " + post_likes)

                $(`#like_post_${post_id}`).empty();
                $(`#like_post_${post_id}`).append(`
                <i class="bi bi-hand-thumbs-up-fill pe-1"></i>Liked (${post_likes})
            `);
            }
        })

    })

    //Like a comment
    $(document).on('click', '.like_comment', function(){

        console.log("comment liked")
        var post_id = $(this).attr("post_id")
        var comment_id = $(this).attr("comment_id")

        console.log(post_id + " " + comment_id)
        $.ajax({type: "POST",
            url:'like_comment/',
            async: false,
            data: {
                post_id: post_id,
                comment_id: comment_id,
                session_id: sessionID
            },
            success: function(response){
                console.log(response)

                if(response == "False"){
                    console.log("Comment is liked by you already") 
                    return 
                }

                console.log('hooo yeahh')
                var comment_num_likes = response.comment_num_likes

                $(`#like_comment_${post_id}_${comment_id}`).empty()
                $(`#like_comment_${post_id}_${comment_id}`).append(`
                Likes(${comment_num_likes})
            `);
            }
        })
    })

    //Fetch the comments when load comments is clicked
    $(document).on('click', '.load_comments', function(){

        var post_id = $(this).attr("post_id")

        fetchComments(post_id)

        $(`#load_comments_${post_id}`).empty()
    })



    function setCookie(cookieName, cookieValue, expirationDays) {
        var d = new Date();
        d.setTime(d.getTime() + (expirationDays * 24 * 60 * 60 * 1000));
        var expires = "expires=" + d.toUTCString();
        document.cookie = cookieName + "=" + cookieValue + ";" + expires + ";path=/";
    }
    
    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
    }
});
