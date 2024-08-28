const display = document.getElementById("display");
const clearBtn = document.getElementById("clear");

function appendToDisplay(input) {
    display.value += input;
    clearBtn.textContent = "C";

    if (display.value.length >= 4) {
        display.style.fontSize = "7em"
    }  if (display.value.length >= 6) {
        display.style.fontSize = "7.5em";
    }  if (display.value.length >= 7) {
        display.style.fontSize = "6em";
    }  if (display.value.length >= 8) {
        display.style.fontSize = "6.5em";
    }  if (display.value.length >= 9) {
        display.style.fontSize = "5em";
    }  if (display.value.length >= 10) {
        display.style.fontSize = "5.5em";
    }  if (display.value.length >= 12) {
        display.style.fontSize = "4em";
    }  if (display.value.length >= 15) {
        display.style.fontSize = "4.5em";
    }  if (display.value.length >= 19) {
        display.style.fontSize = "3em";
    }  if (display.value.length >= 20) {
        display.style.fontSize = "3.5em";
    }  if (display.value.length >= 25) {
        display.style.fontSize = "2em";
    }
}

function clearDisplay() {
    display.value = "";
    display.style.fontSize = "10em";
    clearBtn.textContent = "AC";
}

function calculate() {
    try {
        display.value = eval(display.value);
    } catch (error) {
        display.value = "Error";
    }

    display.style.fontSize = "10em";
}