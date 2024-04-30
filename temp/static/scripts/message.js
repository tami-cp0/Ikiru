$(document).ready(() => {
  const id = $('.container').attr('id');
  let other_id;

  if (id === "d6ac8acc-99bf-493a-a292-88332db8739a") {
    other_id = "a7960df0-ae8e-4a1a-b834-f33322e96792"
  } else {
    other_id = "d6ac8acc-99bf-493a-a292-88332db8739a" // ayo
  }

  console.log('id')
  console.log(id)
  console.log('other id')
  console.log(other_id)

  let socket = io.connect("http://127.0.0.1:5001")
  socket.on('connect', () => {
      socket.send("User connected!");
  });

  // const sender = '.' + $('.footer button').attr('id')
  // console.log(sender);
  $('#send').on('click', () => {
    if ($('#message').val() !== '') {
      socket.send($('#message').val());
      $('#message').val('');
    }  
  });

  socket.on('message', function(data) {
    if (data.trim() !== '') {
      $('.container .body').append($('<div class="messages" id="sent">').html('<p>' + data + '</p>'));
      // Set scroll bar position
      var container = document.getElementById("chat-container");
      container.scrollTop = container.scrollHeight;

      $.post({
        url:`http://127.0.0.1:5000/api/v1/${id}/${other_id}/conversations/16e33d8b-b902-44eb-afb5-e66d25cdd3ab`,
        contentType: 'application/json',
        data: JSON.stringify({'content': data}),
        error: function (xhr, status, error) {
          // Handle error
          console.error('Error:', error);
        }
      });
    }
  });
  // 5a4ab977-a207-4a1f-b024-1c508f277aa0
  // const get = $.get('http://web-01.tamilore.tech/api/v1/users/id/conversations/id/messages')

  // async function get() {

  // }


  // document.addEventListener('DOMContentLoaded', async function(event) {
  //   console.log("===============DOMContentLoaded=============================")
    
  // });



  if (window.performance.getEntriesByType) {
    const navigationEntry = window.performance.getEntriesByType("navigation")[0];
    if (["reload", "navigate", "back_forward"].includes(navigationEntry.type)) {
      console.log("Page was reloaded or loaded via navigation");
      async function get_msg() {
        const messages = await $.get(`http://127.0.0.1:5000/api/v1/users/${id}/conversations/16e33d8b-b902-44eb-afb5-e66d25cdd3ab/messages`)
        return messages;
      }

      async function display_msg() {
        const messages = await get_msg();
        $('.container .body').empty();

        for (const message of messages) {
            if (message.user_id === id) {
                $('.container .body').append($('<div class="messages" id="recieve">').html('<p>' + message.content + '</p>'));
            } else {
                $('.container .body').append($('<div class="messages" id="sent">').html('<p>' + message.content + '</p>'));
            }
        }
        // Set scroll bar position
        var container = document.getElementById("chat-container");
        container.scrollTop = container.scrollHeight;
      }
      display_msg();
    }
  }
});