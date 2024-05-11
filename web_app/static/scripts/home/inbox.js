async function get_html (data) {
  let chat_html;

  await $.get({
    url: `https://web-01.tamilore.tech/api/v1/users/${id}/conversations/${data.id}/messages`,
    contentType: 'application/json',
  })
  .done(function (responses) {
    const updated_at = responses[responses.length -1].updated_at;
    let receiver = data.participants[1];

    if (receiver.receiver_id === id) {
      receiver = data.participants[0];
    }

    let hours = parseInt(updated_at.split("T")[1].substring(0, 2), 10);
    let suffix = "AM";

    if (hours >= 12 && hours < 24) {
      suffix = "PM";
      hours -= 12;
    } else if (hours === 24) {
      hours -= 24
    }

    time = hours.toString() + updated_at.split("T")[1].substring(2, 5) + suffix

    chat_html = `<div class="chat">
    <figure class="chat-profile-pic">
      <img src="../static/images/anonRectangle160.png" alt="Profile pic" />
    </figure>
    <div class="chat-details">
      <div>
        <p>${receiver.name}</p>
        <p>${time}</p>
      </div>
      <p id="${receiver.receiver_id}" style="display: none;"></p>
      <p class="message">${responses[responses.length -1].content}.</p>
    </div>
    <svg
      class="big-red-dot"
      viewBox="0 0 10 10"
      xmlns="https://www.w3.org/2000/svg"
    >
      <rect width="10" height="10" rx="5" fill="#E13E3E" />
    </svg>
    </div>`

  })
  .fail(function(xhr, status, error) {
      console.error('Error:', error);
  });

  return chat_html;
}


async function get_convos (tag) {
  await $.get({
    url: `https://web-01.tamilore.tech/api/v1/users/${id}/conversations`,
    contentType: 'application/json',
  })
  .done(async function (responses) {
    for (response of responses) {
      const sender_id = response.participants[0].sender_id;
      const receiver_id = response.participants[1].receiver_id;
      const my_messages = response.participants[1].messages;

      if (tag === "friends"){
        if (receiver_id === id && my_messages === 0) {
          continue;
        }
      } else {
        if (sender_id === id || my_messages > 0) {
          continue
        }
      }

      chat_html = await get_html(response);
      $('.chat-container').prepend(chat_html);
    }
  })
  .fail(function (xhr, status, error) {
      console.error('Error:', error);
  });
}

if (window.performance.getEntriesByType) {
  const navigationEntry = window.performance.getEntriesByType("navigation")[0];
  if (["reload", "navigate"].includes(navigationEntry.type)) {
    $('.tag-highlight:nth-child(2)').css('background', 'none');
    get_convos("friends");
  }
}

$(document).ready( () => {
  $('#friends-tag').on('click', () => {
    $('.chat-container').empty();
    $('.tag-highlight:first-child').css('background', 'var(--tag-highlight)');
    $('.tag-highlight:nth-child(2)').css('background', 'none');
    get_convos("friends");
  });

  $('#requests-tag').on('click', () => {
    $('.chat-container').empty();
    $('.tag-highlight:first-child').css('background', 'none');
    $('.tag-highlight:nth-child(2)').css('background', 'var(--tag-highlight)');

    get_convos("requests");
  });
});
