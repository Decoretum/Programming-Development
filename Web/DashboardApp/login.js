let uname = '';
let age = '';
let password = '';
let sex = '';

let create = document.getElementById('create');
create.addEventListener('click',function(){
    window.location.href="../DashboardApp/signup.html";
})
/* for (let i = 0; i < window.sessionStorage.length; i++){
    console.log(window.sessionStorage.key(i));
    if (window.sessionStorage.key(i) === "Username"){
        uname = window.sessionStorage.getItem(window.sessionStorage.key(i));
    }
}
let welcome = document.getElementById('welcome');
welcome.innerHTML = `Welcome, user ${uname}`;
*/