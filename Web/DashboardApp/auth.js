//signup 
let Q1 = 0;
let more = document.querySelector('.more');
let info = document.querySelector('.info');
more.addEventListener('mouseover',function(){
    info.innerHTML = "A good user identification must be respectful and non-discriminatory! Don't use fake aliases as well.";
    info.style.width = '20vh';
    info.style.padding = '10px';
    info.style.borderRadius = '12px';
    info.style.backgroundColor = 'azure';
    info.style.boxShadow = '10px 10px';
})
more.addEventListener('mouseleave',function(){
    info.style.height = '';
    info.style.border = '';
    info.innerHTML = '';
    info.style.backgroundColor = '';
    info.style.boxShadow = '';
})
