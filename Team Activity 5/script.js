function pressKey(value) {
  document.getElementById('result').value += value;
}

function calculate() {
  let expression = document.getElementById('result').value;
  try {
    let result = eval(expression);
    document.getElementById('result').value = result;
  } catch (e) {
    document.getElementById('result').value = 'Error';
  }
}

function clearDisplay() {
  document.getElementById('result').value = '';
}