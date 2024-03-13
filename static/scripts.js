// static/scripts.js

/**
 * Send a calculation request to the server.
 * @param {string} operation - The operation to perform: 'add', 'subtract', 'multiply', 'divide'.
 */
function performCalculation(operation) {
    const number1 = parseFloat(document.getElementById('number1').value);
    const number2 = parseFloat(document.getElementById('number2').value);
    const requestData = { operation, number1, number2 };

    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestData),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        if (data.error) {
            displayError(data.error);
        } else {
            displayResult(data.result);
        }
    })
    .catch(error => {
        displayError('An error occurred while processing the calculation.');
        console.error('There has been a problem with your fetch operation:', error);
    });
}

/**
 * Send a reset request to the server to reset the calculator.
 */
function sendResetRequest() {
    fetch('/reset', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        clearInputsAndResult();
        displayMessage(data.message);
    })
    .catch(error => {
        displayError('An error occurred while resetting the calculator.');
        console.error('There has been a problem with your fetch operation:', error);
    });
}

/**
 * Display the calculation result in the UI.
 * @param {number} result - The result to display.
 */
function displayResult(result) {
    const resultElement = document.getElementById('result');
    resultElement.textContent = `Result: ${result}`;
    clearError();
}

/**
 * Display an error message in the UI.
 * @param {string} message - The error message to display.
 */
function displayError(message) {
    const errorElement = document.getElementById('error');
    errorElement.textContent = message;
}

/**
 * Clear any displayed error message.
 */
function clearError() {
    const errorElement = document.getElementById('error');
    errorElement.textContent = '';
}

/**
 * Clear the input fields and the result display.
 */
function clearInputsAndResult() {
    document.getElementById('number1').value = '';
    document.getElementById('number2').value = '';
    document.getElementById('result').textContent = 'Result: ';
    clearError();
}

/**
 * Display a message in the UI.
 * @param {string} message - The message to display.
 */
function displayMessage(message) {
    console.log(message);
}

// Event listeners for calculator buttons
document.addEventListener('DOMContentLoaded', function() {
    const addButton = document.getElementById('addButton');
    const subtractButton = document.getElementById('subtractButton');
    const multiplyButton = document.getElementById('multiplyButton');
    const divideButton = document.getElementById('divideButton');

    addButton.addEventListener('click', () => performCalculation('add'));
    subtractButton.addEventListener('click', () => performCalculation('subtract'));
    multiplyButton.addEventListener('click', () => performCalculation('multiply'));
    divideButton.addEventListener('click', () => performCalculation('divide'));
});
