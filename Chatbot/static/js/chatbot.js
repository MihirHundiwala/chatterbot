var element = document.getElementById("chatwindow");

function getresponse(){
	var input=document.getElementById("user_input").value;
	if(input=="" || input==null)
   {
		return false;
	}
	var userdiv = document.createElement('div');
	userdiv.innerHTML='<p class="user_msg">'+input+'</p>';
	document.getElementById("chatwindow").appendChild(userdiv);
  element.scrollTop = element.scrollHeight;
	document.getElementById("user_input").value="";
      input.placeholder="";
	$.ajax({
            url: 'get_response_from_bot',
            method:'post',
            data: { input:input.toString() },
            success:function(response)
            {
            	if (response=="" || response==null)
            	{
            		return false;
            	}
            	var botdiv=document.createElement('div');
				   botdiv.innerHTML='<p class="bot_msg">'+response+'</p>';
				   document.getElementById("chatwindow").appendChild(botdiv);
               element.scrollTop = element.scrollHeight;
            }
    });
}

document.getElementById("user_input").addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
      var input=document.getElementById("user_input").value;
      if(input=="" || input==null)
      {
        console.log("hi");
        return false;
      }
      getresponse();
      document.getElementById("user_input").value="";
      return false;
    }
});