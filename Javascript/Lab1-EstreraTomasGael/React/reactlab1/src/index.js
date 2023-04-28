import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import Form from './Form';
import Formresult from './Formresult'
import reportWebVitals from './reportWebVitals';

let name1 = "Gael";
class Student extends React.Component{
  constructor(props){
      super(props);
      this.state = {
          Passion : 'Programming'
      }
  }
  render() {
      return(
          <p> {name1} enjoys {this.state.Passion} <br></br>
          This has been his hobby since 2nd year College. He wants to be a powerful
          back-end developer. <br></br><br></br>
          </p>
      )
  }
}

const root = ReactDOM.createRoot(document.getElementById('root'));
const form = ReactDOM.createRoot(document.getElementById('Form'));

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

form.render(
  <React.StrictMode>
    <Form /> <br></br>
    <Student />
    <Formresult />
  </React.StrictMode>
)




// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
