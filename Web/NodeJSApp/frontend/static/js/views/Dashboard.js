import base from "./base.js";

export default class extends base{
     constructor(){
      super();
        this.setTitle("Dashboard");
     }

     async getHTML(){
        return `<h1> This is the Dashboard page baby! </h1>`;
     }
}