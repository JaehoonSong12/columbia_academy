/** * THE APP LAB "LIBRARY" (Emulation Layer)
 * These functions allow you to use your original CSP code.
 */
function onEvent(id, type, callback) {
  const el = document.getElementById(id);
  if (el) el.addEventListener(type, callback);
}

function setText(id, text) {
  const el = document.getElementById(id);
  if (el) el.textContent = text;
}

function setProperty(id, prop, value) {
  const el = document.getElementById(id);
  if (el) el.style[prop] = value;
}



document.addEventListener('DOMContentLoaded', () => {
  /**
   * This is where your school editor will recognize.
   */
  var answers = [
    "Signs point to yes.", "Yes, definitely.", "Most likely.", "Outlook good.",
    "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
    "Don't count on it.", "My sources say no.", "Very doubtful."
  ];
  // Fixed the arrow function typo from your screenshot
  onEvent("magicEightBall", "click", function() {
    setText("resultText", "Thinking...");
    
    setTimeout(function() {
      var randomIndex = Math.floor(Math.random() * answers.length);
      setText("resultText", answers[randomIndex]);
    }, 400);
  });


  
});
