$(() => {
    socket = io.connect("http://127.0.0.1:5000");
    convoio = io.connect("http://127.0.0.1:5000/home/${username}");
  
  
    convoio.on("private", () => {
      convo_contianer = $("get the coversation selector")
  
    });
  
  // this listen to post user posted on "http://127.0.0.1:5000/home" socket
    socket.on("post", () => {
  
    });
  
    //post using socket connected to http://127.0.0.1:5000/home
    // everyone that his/her socket connected using http://127.0.0.1:5000/home and listening receive the post instantly
    $().on("click", () => {
      
      // send the post to backend eventlistener "post"
      socket.emit("post", data);
    });
  
    inboxio = io.connect("http://127.0.0.1:5000/msg/${my_username}");
    // send
    $("#send").on("click", () => {
  
      socket.emit("sent_message", data);
    });
});