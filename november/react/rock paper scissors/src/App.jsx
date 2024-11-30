// import React from "react";
import "./App.css";

const App = () => {
  const myScoreP = document.getElementById("my-score");
  const compScoreP = document.getElementById("comp-score");
  const winsP = document.getElementById("wins");
  const btnsDiv = document.getElementById("btns");

  const choices = ["rock", "paper","scissors"];

  let myScore = 0;
  let compScore = 0;

  btnsDiv.addEventListener("click", (e) => {
      const btnId = e.target.id;

      const compChoice = choices[Math.floor(Math.random() * choices.length)];

      if(btnId === compChoice) {
          winsP.textContent = "Its a tie!";
          myScoreP.textContent = `Your score: ${myScore}`;
      } 
      
      else if((btnId === "rock" && compChoice === "paper") || (btnId === "scissors" && compChoice === "rock") || (btnId === "paper" && compChoice === "scissors")) {
          compScore++;
          compScoreP.textContent = `Computer score: ${compScore}`;
          winsP.textContent = "You lost!";
      } 
      
      else {
          myScore++;
          myScoreP.textContent = `Your score: ${myScore}`;
          winsP.textContent = "You won!";
      }
  });
  
  return (
      <main>
        <h1>Welcome to rock, paper, scissors!</h1>
        <div>
            <p id="my-score">Your score: 0</p>
            <p id="comp-score">Computer score: 0</p>
        </div>
        <br />
        <p id="wins">Click Button To Start</p>
        <br />
        <div id="btns">
            <button id="rock">Rock</button>
            <button id="paper">Paper</button>
            <button id="scissors">Scissors</button>
        </div>
        <br />
        <div id="images">
          <img src="./src/assets/rock.png" alt="rock" />
          <img src="./src/assets/paper.png" alt="paper" />
          <img src="./src/assets/scissors.png" alt="scissors" />
        </div>
    </main>
  )
}

export default App;