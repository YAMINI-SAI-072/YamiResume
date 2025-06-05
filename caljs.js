const display = document.getElementById("display");

function appendValue(value) {
  display.value += value;
}

function clearDisplay() {
  display.value = '';
}

function calculate() {
  try {
    display.value = eval(display.value);
  } catch {
    display.value = 'Error';
  }
}

function calculatePercentage() {
  try {
    display.value = eval(display.value) / 100;
  } catch {
    display.value = 'Error';
  }
}

function square() {
  try {
    display.value = Math.pow(eval(display.value), 2);
  } catch {
    display.value = 'Error';
  }
}

function squareRoot() {
  try {
    display.value = Math.sqrt(eval(display.value));
  } catch {
    display.value = 'Error';
  }
}

function toggleSign() {
  try {
    display.value = eval(display.value) * -1;
  } catch {
    display.value = 'Error';
  }
}

function backspace() {
  display.value = display.value.slice(0, -1);
}
