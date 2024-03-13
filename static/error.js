// static/error.js

/**
 * Display an error message in the UI.
 * @param {string} message - The error message to display.
 */
function displayError(message) {
    const errorElement = document.getElementById('error');
    errorElement.textContent = message;
    errorElement.style.display = 'block'; // Ensure the error message is visible
}

/**
 * Clear any displayed error message.
 */
function clearError() {
    const errorElement = document.getElementById('error');
    errorElement.textContent = '';
    errorElement.style.display = 'none'; // Hide the error message element
}

// Export the functions for use in other scripts if this file is included as a module
if (typeof module !== 'undefined' && typeof module.exports !== 'undefined') {
    module.exports = {
        displayError,
        clearError
    };
}
