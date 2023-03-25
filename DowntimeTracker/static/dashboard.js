const progressBar = document.getElementById("my-progress-bar");
const percentage = parseInt(progressBar.getAttribute('data-percentage'));
progressBar.style.width = percentage + '%';1
