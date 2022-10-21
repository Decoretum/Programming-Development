let randomNumber = Math.floor(Math.random() * 100) + 1;
//constants and variables
const guesses = document.querySelector('.guesses');
const lastResult = document.querySelector('.lastResult');
const lowOrHi = document.querySelector('.lowOrHi');
//inside div class resultparas
const guessSubmit = document.querySelector('.guessSubmit');
const guessField = document.querySelector('.guessField');
let count = 0;
let guessCount = 1;
let resetButton;

// .textcontent and .value used to represent data of constants from HTML fields
// use Number() to get integer from argument

function checkGuess() {
    const userGuess = Number(guessField.value);
    if (guessCount === 1) {
      guesses.textContent = 'Previous guesses: ';
    }
    guesses.textContent += ' ' + userGuess;
  
    if (userGuess === randomNumber) {
      lastResult.textContent = 'Congratulations! You got it right!';
      lastResult.style.backgroundColor = 'green';
      lowOrHi.textContent = '';
      count++
      const count1 = document.querySelector('.counter'); //counter
      count1.textContent = `${count}`

      setGameOver();
    } 
    else if (guessCount === 10) {
      lastResult.textContent = '!!!GAME OVER!!!';
      lowOrHi.textContent = '';
      setGameOver();
    } 
    else {
      lastResult.textContent = 'Wrong!';
      lastResult.style.backgroundColor = 'red';
      if (userGuess < randomNumber) {
        lowOrHi.textContent = 'Last guess was too low!';
      } 
      else if (userGuess > randomNumber) {
        lowOrHi.textContent = 'Last guess was too high!';
      }
    }
  
    guessCount++;
    guessField.value = '';
    guessField.focus();
  }


function setGameOver() {
  guessField.disabled = true;
  guessSubmit.disabled = true;
  resetButton = document.createElement('button'); //creation of new element for HTML
  resetButton.textContent = 'Start new game'; 
  document.body.append(resetButton); //adding new element to HTML
  resetButton.addEventListener('click', resetGame);
}


function resetGame() {
  guessCount = 1; //resets guessCount

  const resetParas = document.querySelectorAll('.resultParas p'); //division class containing the paragraphs in HTML
  for (const p of resetParas) {
    p.textContent = '';
  }

  resetButton.parentNode.removeChild(resetButton); //HTML button removes itself

  guessField.disabled = false;
  guessSubmit.disabled = false;
  guessField.value = '';
  guessField.focus();

  lastResult.style.backgroundColor = 'white';

  randomNumber = Math.floor(Math.random() * 100) + 1;
}

guessSubmit.addEventListener('click',checkGuess) //calling out guessSubmit constant


let promise1 = new Promise(function(resolve,reject){
  for (i=0; i<[1,2,3,4,5].length;i++){
  console.log(i*i);
  
  }
resolve('Done!')
reject('Damn!') 
})
.finally(cute)
.then(result => console.log(result),
       error => alert(error))
.then(cute,
dead => console.log('Dead!'))

function cute(){
  console.log('Aw this is cute!')
}

console.log(promise1)