let testing = document.querySelector('.timer');
function time(){
    let timearea = '';
    const now = new Date();
    let seconds = now.getSeconds();
    let minutes = now.getMinutes();
    let hours = now.getHours();

    if (seconds < 10){
        seconds = '0' + now.getSeconds();
    }
    if (minutes < 10){
        minutes = '0' + now.getMinutes();
    }
    if (hours < 10){
        hours = '0' + now.getHours();
    }

    if (hours >= 12){
        timearea = 'PM';
    }
    else{
        timearea = 'AM';
    }
    testing.textContent = `${hours} : ${minutes} : ${seconds} ${timearea}`;
    testing.classList.add('timer');
};

setInterval(time,1000);