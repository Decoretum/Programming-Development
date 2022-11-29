let head = document.getElementById('head');
let popup = document.getElementById('popup');
head.addEventListener('mouseover',()=>{
    console.log("Hovered!");
    popup.innerHTML = "Don't forget to stay tuned to Gael's development updates on web development and/or other programming assessments!";
    popup.style.color='black';
    popup.style.backgroundColor = 'green';
    popup.style.padding = '9px';
    popup.style.borderRadius = '9px';
    
})
head.addEventListener('mouseleave',()=>{
    popup.innerHTML='';
    popup.style.color='';
    popup.style.backgroundColor = '';
    
})

