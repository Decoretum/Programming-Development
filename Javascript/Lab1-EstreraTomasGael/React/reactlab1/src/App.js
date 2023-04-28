import './App.css';
import './Form.js';


let name = "Gael";

let Person = {
  Hobby: 'Programming & Speedcubing',
  Course: 'BS MIS',
  Spec: 'Enterprise Systems'
}

let comment = (
  <p> I want to be the very best! </p>
)

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Welcome to {name}'s first React front-end app! <br></br>
          {name}'s hobby is {Person.Hobby} with a course of {Person.Course}, {Person.Spec}. 
        </p>
        <a
          className="App-link"
          href="https://github.com/Decoretum"
          target="_blank"
          rel="noopener noreferrer"
        >
          Gael's Github Account
        </a>
        <br></br>
      </header>
    </div>

    
  );
}

export default App;
