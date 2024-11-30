// import React from "react";
import "./App.css";

const App = () => {
  const form = document.querySelector("form");
  const ul = document.getElementById("tasks");
  const message = document.querySelector("span");
  const darkmodeBtn = document.querySelector("#btn")
  const lightmodeBtn = document.querySelector("#btn2");
  const background = document.querySelector("body");
  const h1 = document.querySelector("h1");
  const h2 = document.querySelector("h2");
  const clear = document.querySelector("#delete");

  let index = 0;

  form.addEventListener("submit", (e) => {
      e.preventDefault();

      const input = form.input.value;

      if (input === "") {
          message.textContent = "Incorrect, Please fill the field to add an task";
          return;
      }

      ul.innerHTML += `<li id=${index}>${input}</li>`;

      index++;
      message.textContent = "";

      form.input.value = "";

      const clearTasks = () => {
          ul.innerHTML = ``;
      }

      clear.onclick = clearTasks;
  })

  ul.addEventListener("click", (e) => {
      if (e.target.tagName === "LI") {
          e.target.remove();
      }
  })

  const darkMode = () => {
      background.style.background = "rgb(24, 24, 24)";
      h1.style.color = "white";
      h2.style.color = "white";
      ul.style.color = "white";
  }

  darkmodeBtn.onclick = darkMode;

  const lightMode = () => {
      background.style.background = "white";
      h1.style.color = "black";
      h2.style.color = "black";
      ul.style.color = "black";
  }

  lightmodeBtn.onclick = lightMode;

  return (
    <>
      <h1>To-do list</h1>
      <br />
      <div className="toogle">
          <h2>Dark mode:</h2>
          <button id="btn">Dark mode</button>
          <button id="btn2">Light mode</button>
      </div>
      <br />
      <form id="form">
          <input type="text" name="input" id="input" placeholder="Enter an task" />
          <button id="add">Add task</button>
          <button id="delete">Delete all tasks</button>
          <br />
          <span id="message"></span>
          <br />
          <ul id="tasks">

          </ul>
      </form>
    </>
  )
}

export default App;