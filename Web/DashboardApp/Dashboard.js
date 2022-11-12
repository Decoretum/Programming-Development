let posts = document.querySelector('.Posts');
let create = document.querySelector('.submit');

let keylist = [];
for (i=0; i < window.localStorage.length; i++){
    keylist.unshift(window.localStorage.key(i));
    console.log(window.localStorage.getItem(window.localStorage.key(i)));
}

for (key of keylist){
    if (key.includes("postcounter")){
        console.log(key[-1]);
    }
}
console.log(keylist);
//window.localStorage.setItem(window.localStorage.getItem('postcounter'),"test");

//posts.innerHTML += `<div style='background-color: antiquewhite'> <div> ${Title} </div> <div> ${Content} </div> </div><br><br>`;
//for (x of window.localStorage.)

let button = document.querySelector('.Create');
button.addEventListener('click',function(){
    document.querySelector('.content').classList.toggle('show');
})

create.addEventListener('click',function(){
    let Title = document.querySelector('.Title').value;
    let Content = document.querySelector('.Body').value;
    //window.localStorage.setItem('')
})