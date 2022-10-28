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




let create = document.getElementById('create');
create.addEventListener('click',function(){
    let Name = document.getElementById('Name').value;
    let Password = document.querySelector('.Password').value;
    let Age = document.querySelector('.Age').value;
    let Sex = document.querySelector('.Sex').value;
    if (Name === '' || Password === '' || Age === '' || Sex === ''){
        console.log("Must complete all fields!");
    }
    else if (window.localStorage.getItem(Name) === null){
        window.localStorage.setItem(Name,Name);
        window.localStorage.setItem(Password,Password);
        window.localStorage.setItem(Age,Age);
        window.localStorage.setItem(Sex,Sex);
        window.location.href='../DashboardApp/login.html';
    }
    else if (window.localStorage.getItem(Name) !== null){
        console.log("User already exists!");

    }
})

