import Dashboard from "./views/Dashboard.js";

let navigate = url => {
    history.pushState(null, null, url);
    router();
}


let router = async () => {
    let routes = [
        {path: "/", view: () => Dashboard},
        {path: "/posts", view: () => console.log("Viewing Posts")},
        {path: "/settings", view: () => console.log("Viewing Settings")},

    ];

    //testing each route for potential match
    let potentialmatch = routes.map(route =>{
        return {
            route: route.view,
            isMatch: location.pathname === route.path
        }
    })

    let match = potentialmatch.find(potential =>potential.isMatch);



    if (!match){
        match ={
            route: routes[0],
            isMatch: true
        }
    }

    let view = new match.route();

    document.querySelector("#app").innerHTML = await view.getHTML();
    console.log(match.view);
};

window.addEventListener('popstate',router);

document.addEventListener('DOMContentLoaded', ()=>{
    document.body.addEventListener('click', e =>{
        if (e.target.matches("[data-link]")){
            e.preventDefault();
            navigate(e.target.href);
        }
    });
    router();
})
