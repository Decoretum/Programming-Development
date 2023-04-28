import logo from './logo.svg';
import './App.css';
import Categories from './Categories';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Data from <a href='https://jservice.io'
          style={{color: 'white'}}
          target='_blank'
          rel='noreferrer'
          >
             JService.io </a> will be displayed on the bottom
        </p>
      </header>

      <Categories />
    </div>
  );
}

export default App;
