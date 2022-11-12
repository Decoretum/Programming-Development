let uname = '';
let age = '';
let password = '';
let sex = '';

let create = document.getElementById('create');
create.addEventListener('click',function(){
    window.location.href="../DashboardApp/signup.html";
})

let login = document.getElementById('login');
login.addEventListener('click',function(){
    let info = document.querySelector('.info');
    let username = document.getElementById('Name').value;
    let password = document.getElementById('Password').value;
    if (username === '' || password === ''){
        info.innerHTML = 'Have to input fields!';
    }
    else if (username !== window.localStorage.getItem(username) || password !== window.localStorage.getItem(password)){
        info.innerHTML = 'Invalid credentials';
    }
    else{
        window.sessionStorage.setItem("Username",Name);   
        window.sessionStorage.setItem("Password",password);
        window.location.href='../DashboardApp/Dashboard.html';
    }
})
