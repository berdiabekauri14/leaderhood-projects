import "./App.css";
import Help from "./Help";

const App = () => {
  const btn = document.getElementById("btn");
  const yearsP = document.getElementById("yearsParagraph");
  const monthsP = document.getElementById("monthsParagraph");
  const daysP = document.getElementById("daysParagraph");
  const message = document.getElementById("message");

  const d = new Date();
  console.log(d);

  const calculateAge = () => {
      const day = document.getElementById("day");
      const month = document.getElementById("month");
      const year = document.getElementById("year");

      if (day.value === "" || month.value === "" || year.value === "") {
          message.textContent = "Incorrect, Please enter in all fields";
          return;
      } else {
          message.textContent = "";
      }

      if (day.value > 31) {
          message.textContent = "Incorrect day value, day must be a number from 1 to 31";
          return;
      } else {
          message.textContent = "";
      }

      if (month.value > 12) {
          message.textContent = "Incorrect month value, month must be from 1 to 12";
          return;
      } else {
          message.textContent = "";
      }

      if (year.value > 2024) {
          message.textContent = "Incorrect year value, year must be less or eqaul to 2024";
          return;
      } else {
          message.textContent = "";
      }

      yearsP.textContent = d.getFullYear() - year.value;
      monthsP.textContent = d.getMonth() - month.value;
      daysP.textContent = d.getDate() - day.value;

      if (d.getDate() < day.value) {
          daysP.textContent = day.value - d.getDate();
      } if (month.value > d.getMonth()) {
          monthsP.textContent = month.value - d.getMonth();
      }
  }

  btn.onclick = calculateAge;

  return (
    <div className="container">
      <div className="inputs">
        <h2>Day</h2>
        <input type="number" id="day" name="day" placeholder="DD" />
        <h2 id="h2">Month</h2>
        <input type="number" id="month" name="month" placeholder="MM" />
        <h2 id="second-h2">Year</h2>
        <input type="number" id="year" name="year" placeholder="YYYY" />
        <br />
        <span id="message"></span>
      </div>
      <br />
      <button id="btn"><svg xmlns="http://www.w3.org/2000/svg" width="46" height="44" viewBox="0 0 46 44"><g fill="none" stroke="#FFF" strokeWidth="2"><path d="M1 22.019C8.333 21.686 23 25.616 23 44M23 44V0M45 22.019C37.667 21.686 23 25.616 23 44"/></g></svg></button>
      <div className="line"></div>
      <br />
      <div className="resultsContainer">
        <h1 className="h1"><i><p id="yearsParagraph" className="par">--</p> <p className="paragraph" id="years">years</p></i></h1>
        <h1 className="h1"><i><p id="monthsParagraph" className="par">--</p> <p id="months" className="paragraph">months</p></i></h1>
        <h1 className="h1"><i><p id="daysParagraph" className="par">--</p> <p id="days" className="paragraph">days</p></i></h1>
      </div>
      <br />
      <Help />
  </div>
  )
}

export default App;