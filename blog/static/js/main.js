// Hiding messages.
function hiding_message(){
    var messageDiv = document.getElementById('message-div');
    messageDiv.style.display = 'none';
}
var interval = setInterval(hiding_message, 5000);