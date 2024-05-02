$(document).ready(() => {
  const id = $('.container').attr('id');
  let other_id;

  if (id === "233bfba0-9195-4509-bea9-e0b716fbeaf4") {
    other_id = "7f772738-33a7-4ba6-aa8a-b74437551806"
  } else {
    other_id = "233bfba0-9195-4509-bea9-e0b716fbeaf4" // tunde
  }

  console.log('id')
  console.log(id)
  console.log('other id')
  console.log(other_id)

  let home = io.connect(`http://127.0.0.1:5001/${id}`)
  let socket = io.connect("127.0.0.1:5001/private")
  socket.on('connect', () => {
      socket.send({"content": "User connected!"});
  });

  // const sender = '.' + $('.footer button').attr('id')
  // console.log(sender);
  $('#send').on('click', async function() {
    const message = $('#message').val()
    if (message !== '') {
      data = await post(message);
      console.log(data);
      socket.send(data);
      $('.container .body').append($('<div class="messages" id="recieve">').html('<p>' + data['content'] + '</p>'));
      var container = document.getElementById("chat-container");
      container.scrollTop = container.scrollHeight;
      $('#message').val('');
    }  
  });

  // $('#')

  // emit()


  // socket.on('message', function(data) {
    
  // });
  let convo_id;
  async function post(message) {
    let json_data;
    await $.post({
      url: `http://127.0.0.1:5000/api/v1/${id}/${other_id}/conversations/None`,
      contentType: 'application/json',
      data: JSON.stringify({'content': message})
    })
    .done(function(response) {
        json_data = {};
        json_data['room'] = response.conversation_id;
        json_data['content'] = response.content;
        const convo_id = response.conversation_id;
        // Now you can work with json_data or do other operations
    })
    .fail(function(xhr, status, error) {
        // Handle error
        console.error('Error:', error);
    });

    // console.log(response);
    // convo_id = await response;
    return json_data;
  }

//   socket.on('message', function(data) {
//     if (data.trim() !== '') {
//       $('.container .body').append($('<div class="messages" id="sent">').html('<p>' + data + '</p>'));
//       // Set scroll bar position
//       var container = document.getElementById("chat-container");
//       container.scrollTop = container.scrollHeight;

//   //     $.post({
//   //       url:`http://127.0.0.1:5000/api/v1/${id}/${other_id}/conversations/16e33d8b-b902-44eb-afb5-e66d25cdd3ab`,
//   //       contentType: 'application/json',
//   //       data: JSON.stringify({'content': data}),
//   //       error: function (xhr, status, error) {
//   //         // Handle error
//   //         console.error('Error:', error);
//   //       }
//   //     });
//   //   }
//   }
//   // 5a4ab977-a207-4a1f-b024-1c508f277aa0
//   // const get = $.get('http://web-01.tamilore.tech/api/v1/users/id/conversations/id/messages')

//   // async function get() {

//   // }


//   // document.addEventListener('DOMContentLoaded', async function(event) {
//   //   console.log("===============DOMContentLoaded=============================")
    
//   });



//   // if (window.performance.getEntriesByType) {
//   //   const navigationEntry = window.performance.getEntriesByType("navigation")[0];
//   //   if (["reload", "navigate", "back_forward"].includes(navigationEntry.type)) {
//   //     console.log("Page was reloaded or loaded via navigation");
//   //     async function get_msg() {
//   //       const messages = await $.get(`http://127.0.0.1:5000/api/v1/users/${id}/conversations/${convo_id}/messages`)
//   //       return messages;
//   //     }

//   //     async function display_msg() {
//   //       const messages = await get_msg();
//   //       $('.container .body').empty();

//   //       for (const message of messages) {
//   //           if (message.user_id === id) {
//   //               $('.container .body').append($('<div class="messages" id="sent">').html('<p>' + message.content + '</p>'));
//   //           } else {
//   //               $('.container .body').append($('<div class="messages" id="recieve">').html('<p>' + message.content + '</p>'));
//   //           }
//   //       }
//   //       // Set scroll bar position
//   //       var container = document.getElementById("chat-container");
//   //       container.scrollTop = container.scrollHeight;
//   //     }
//   //     display_msg();
//   //   }
//   // }
 });