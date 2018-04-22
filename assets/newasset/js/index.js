var send = document.querySelector('.chatbox__input svg');
var body = document.querySelector('.chatbox__body')
var input = document.querySelector('input');

var messageController = (function(){

  var starkQuotes = [
    "I TOLD YOU. I DON’T WANT TO JOIN YOUR SUPER-SECRET BOY BAND.",
    "I LOVED YOU IN A ‘A CHRISTMAS STORY’.",
    "WELL, PERFORMANCE ISSUES, IT’S NOT UNCOMMON. ONE OUT OF FIVE…",
    "I’M A HUGE FAN OF THE WAY YOU LOSE CONTROL AND TURN INTO AN ENORMOUS GREEN RAGE MONSTER.",
    "HOW DO YOU GO TO THE BATHROOM IN THE SUIT?” [LONG PAUSE.] “JUST LIKE THAT.",
    "DOTH MOTHER KNOW YOU WEARETH HER DRAPES.",
    "SOMETIMES YOU GOTTA RUN BEFORE YOU CAN WALK.",
    "HAVE YOU EVER TRIED SHAWARMA… I DON’T KNOW WHAT IT IS, BUT I WANNA TRY IT.",
    "IF THERE’S ONE THING I’VE PROVEN IT’S THAT YOU CAN COUNT ON ME TO PLEASURE MYSELF.",
    "WE HAVE A HULK.",
    "GENIUS, BILLIONAIRE, PLAYBOY, PHILANTHROPIST.",
    "I AM IRON MAN"
  ];

  return {
    sendMessage: function(){
      var message_container = document.createElement("div");
      var message = `<img src="/static/student.png"/>
      <div class="message_text"> ${input.value} </div>`;
      message_container.className = "message sender";
      message_container.innerHTML = message;
      body.insertBefore(message_container, body.firstChild);
      input.value = "";
    },
    starkReply: function(){
      //var reply = starkQuotes[Math.floor(Math.random() * starkQuotes.length-1) + 1];
    /*  var reply= $.get("/getresponse", function(req, data) {
          console.log('data--'+data);
          console.log($.parseJSON(data['str']));
        });*/
        var reply="";
        $.ajax({
        url: 'getresponse/',
        dataType: 'json',
        success: function (data) {
            reply=data['res'];
            console.log(data);
            var message_container = document.createElement("div");
            var message = `<img src="https://cdn1.chatbottutorial.com/wp-content/uploads/2017/05/25205205/surveybot-web.jpg"/>
            <div class="message_text"> ${reply} </div>`;
            message_container.className = "message receive";
            message_container.innerHTML = message;
            body.insertBefore(message_container, body.firstChild);
        }
      });
    }
  }
})();

var init = (function(messageController){
  ['click', 'keyup'].forEach(event => document.addEventListener(event, handler));

  function handler(e){
      if(e.target == send  || e.keyCode == 13 ){
      messageController.sendMessage();
      setTimeout(messageController.starkReply, 1000);
    }
  }
})(messageController);
