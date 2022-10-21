//Get elements 
const player = document.querySelector('.player');
const video = document.querySelector('.viewer'); //video itself
const progress = document.querySelector('.progress');
const progressbar = document.querySelector('.progress__filled');
const toggle = document.querySelector('.toggle');
const slider = document.querySelectorAll('.player__slider');
const ranges = document.querySelectorAll('.player__button');
const skips = document.querySelectorAll('[data-skip]');

// Build functions

function toggleplay(){
if (video.paused){ //video properties
    video.play(); //video functions

}else{
    video.pause();
}
}

function updatebutton(){
const icon = this.paused ? '►' : '||'; //if true then there. else, 
toggle.innerHTML = icon;
}

function skipit(){
    console.log(this.dataset.skip); //this is the value of the dataset, which is skip
    video.currentTime += parseFloat(this.dataset.skip); //video properties, parsefloat to convert integer into float to get true value
  
}

function handleRange(){
console.log(video[this.name]);
video[this.name] = this.value; //video has these properties

}

function handleProgress(){
    const percent = (video.currentTime / video.duration) * 100 //we get percentage of current time respect to duration
    progressbar.style.flexBasis = `${percent}%`;
}

function progressCalculate(e){ //we find the value of the offset x of the progress bar
const Time = (e.offsetX / progress.offsetWidth) * video.duration; //we take mouse pointer event position and divide it by max width of element multiplied to vid duration for the percentage
video.currentTime = Time;
}

// Hook up event listeners

toggle.addEventListener('click',toggleplay); //will play video when we click toggle button

//these are events of videos we are listening
video.addEventListener('click',toggleplay);
video.addEventListener('play',updatebutton);
video.addEventListener('pause',updatebutton);
video.addEventListener('timeupdate', handleProgress);

let mousedown = false;
progress.addEventListener('click', progressCalculate);
progress.addEventListener('mousedown', (e) => mousedown && progressCalculate(e)); //if mousedown true, then we proceed to calculate
progress.addEventListener('mousedown', () => mousedown = true);
progress.addEventListener('mouseup', () => mousedown = false);


skips.forEach(skip => skip.addEventListener('click',skipit)); //we listen to every skip button element
slider.forEach(slide => slide.addEventListener('change',handleRange)); //elements with type "range" listen to change events
slider.forEach(slide => slide.addEventListener('mousemove',handleRange));