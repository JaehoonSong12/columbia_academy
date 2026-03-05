const answers = [
  "Signs point to yes.",
  "Yes, definitely.",
  "Most likely.",
  "Outlook good.",
  "Reply hazy, try again.",
  "Ask again later.",
  "Better not tell you now.",
  "Don't count on it.",
  "My sources say no.",
  "Very doubtful."
];

document.addEventListener('DOMContentLoaded', () => {
  const ball = document.getElementById('magicEightBall');
  const result = document.getElementById('resultText');

  if (ball && result) {
    ball.addEventListener('click', () => {
      result.textContent = "Thinking...";
      
      setTimeout(() => {
        const randomIndex = Math.floor(Math.random() * answers.length);
        result.textContent = answers[randomIndex];
      }, 400);
    });
  }
});
