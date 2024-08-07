function populate_post (data) {
  // function that prepares and returns html for prepending  
    const name = $('.user-details .username').text();
    const post_html = `<article class="post">
          <div class="left-side">
            <figure id="post-profile-pic">
              <a href="/${data.username}"><img src="../static/images/anonRectangle160.png" alt="Profile picture" /></a>
            </figure>
            <div class="thread"></div>
          </div>
          <div class="content">
            <p class="name"><a href="/${data.username}">${name}</a></p>
            <p class="post-text">${data.content}</p>
            <p class="id" id="{{ post.id }}" style="display: none;"></p>
            <div class="post-interaction">
              <div class="like">
                <svg
                  class="like-button post-interaction-buttons"
                  viewBox="0 0 24 24"
                  xmlns="https://www.w3.org/2000/svg"
                >
                  <path
                    class="like-button-path"
                    d="M19 14C20.49 12.54 22 10.79 22 8.5C22 7.04131 21.4205 5.64236 20.3891 4.61091C19.3576 3.57946 17.9587 3 16.5 3C14.74 3 13.5 3.5 12 5C10.5 3.5 9.26 3 7.5 3C6.04131 3 4.64236 3.57946 3.61091 4.61091C2.57946 5.64236 2 7.04131 2 8.5C2 10.8 3.5 12.55 5 14L12 21L19 14Z"
                  />
                </svg>
                <span></span>
              </div>
              <div class="comment">
                <svg
                  class="comment-button post-interaction-buttons"
                  viewBox="0 0 23 20"
                  xmlns="https://www.w3.org/2000/svg"
                >
                  <path
                    class="comment-button-path"
                    d="M21.6925 9.41474C21.6965 10.7227 21.342 12.013 20.6579 13.1805C19.8468 14.5796 18.5999 15.7563 17.0568 16.579C15.5137 17.4016 13.7354 17.8376 11.9211 17.8382C10.4038 17.8416 8.90697 17.5361 7.55263 16.9463L1 18.8292L3.18421 13.1805C2.50013 12.013 2.14563 10.7227 2.14958 9.41474C2.15019 7.8507 2.65611 6.31772 3.61038 4.9875C4.56466 3.65728 5.92971 2.58236 7.55263 1.88314C8.90697 1.29343 10.4038 0.987829 11.9211 0.991239H12.4958C14.892 1.1052 17.1552 1.97705 18.8521 3.43986C20.549 4.90167 21.5603 6.85365 21.6925 8.91924V9.41474Z"
                  />
                </svg>
                <span><span class="comment-count">0<span> comments</span>
                </span>
              </div>
              <div class="save">
                <svg
                  class="save-button"
                  viewBox="0 0 19 21"
                  xmlns="https://www.w3.org/2000/svg"
                >
                  <path
                    class="save-button-path"
                    d="M17.0942 19.8199L9.04709 14.8649L1 19.8199V3.96393C1 3.43827 1.24223 2.93414 1.67341 2.56245C2.10459 2.19075 2.68939 1.98193 3.29917 1.98193H14.795C15.4048 1.98193 15.9896 2.19075 16.4208 2.56245C16.8519 2.93414 17.0942 3.43827 17.0942 3.96393V19.8199Z"
                  />
                </svg>
                <span>Save</span>
              </div>
              <div class="share">
                <svg
                  class="share-button"
                  viewBox="0 0 24 21"
                  xmlns="https://www.w3.org/2000/svg"
                >
                  <path
                    class="share-button-path"
                    d="M1 9.919L22.8421 1L12.4958 19.829L10.1967 11.901L1 9.919Z"
                  />
                </svg>
                <span>Share</span>
              </div>
            </div>
          </div>
        </article>`

  return post_html;
}

$(document).ready( () => {
  $(document).on('click', '.counter-post', async function() {
    console.log('osds');
    content = $('.express-input-area textarea').val();
    let json_response;

    // if textarea is not empty
    if (content != '') {
      await $.post({
        url:`https://web-01.tamilore.tech/api/v1/users/${id}/posts`,
        contentType: 'application/json',
        data: JSON.stringify({'content': content}),
        success: function (response) {
          json_response = populate_post(response);

          $('.feed-section').prepend(json_response);
          $('.post-section').prepend(json_response);
          // notify user that the upload is successful
          $('.success.status-container').css('opacity', '100%');

          setTimeout(function() {
            $('.success.status-container').fadeOut(1000);
          }, 1000);
        },
        error: function (xhr, status, error) {
          console.error('Error:', error);

          // notify user that the upload failed
          $('.fail.status-container').css('opacity', '100%');
          setTimeout(function() {
            $('.fail.status-container').fadeOut(1000);
          }, 1000);
        }
      });
    
      // reset textarea
      $('.express-input-area textarea').val('');
    }
  });
});


