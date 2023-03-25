const totalDays = 100;
const daysCompleted = 50;
const progressBar = document.querySelector('.progress-bar');
const percent = Math.round(daysCompleted / totalDays * 100);
progressBar.style.width = percent + '%';
progressBar.setAttribute('aria-valuenow', percentage);