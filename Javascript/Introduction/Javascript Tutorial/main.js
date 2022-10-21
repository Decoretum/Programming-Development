// 1. COMPLETE VARIABLE AND FUNCTION DEFINITIONS

const customName = document.getElementById('customname');
const randomize = document.querySelector('.randomize');
const story = document.querySelector('.story');

function randomValueFromArray(array){
  const random = Math.floor(Math.random()*array.length);
  return array[random];
}



// 2. RAW TEXT STRINGS

const insertX = ['Willy the Goblin','Big Daddy','Father Christmas'];
const insertY = ['the soup kitchen','Disneyland','the White House'];
const insertZ = ['spontaneously combusted','melted into a puddle on the sidewalk','turned into a slug and crawled away'];
const storyText = 'It was 94 fahrenheit outside, so :insertx: went for a walk. When they got to :inserty:, they stared in horror for a few moments, then :insertz:. Bob saw the whole thing, but was not surprised — :insertx: weighs 300 pounds, and it was a hot day.';


// 3. EVENT LISTENER AND PARTIAL FUNCTION DEFINITION

randomize.addEventListener('click', result);

function result() {
    let newStory = storyText; // new story each time button is pressed
    const xitem = randomValueFromArray(insertX);
    const yitem = randomValueFromArray(insertY);
    const zitem = randomValueFromArray(insertZ);
    const newStory1 = newStory
    .replaceAll(':insertx:', xitem)
    .replaceAll(':inserty:', yitem)
    .replaceAll(':insertz:', zitem);


  if(customName.value !== '') {
    const name = customName.value;
    let newStory2 = newStory1.replaceAll('Bob', name);

    if(document.getElementById("uk").checked) { // 1 pound = 0.0714286 stone   while  1 farenheit = -17.2222 celsius
      const weight = Math.round(300 * 0.0714286 ) + ' stone'; //stone
      const temperature =  Math.round(94 * -17.2222) + ' centigrade'; //centigrade or celsius
      let newStory3 = newStory2
      .replaceAll('94 fahrenheit', temperature)
      .replaceAll('300 pounds', weight);
      story.textContent = newStory3;

  }
    else{
      let newStory3 = newStory2;
      story.textContent = newStory3;

    }
}

  else{
    let newStory2 = newStory1;
    if(document.getElementById("uk").checked) { // 1 pound = 0.0714286 stone   while  1 farenheit = -17.2222 celsius
      const weight = Math.round(300 * 0.0714286 ) + ' stone'; //stone
      const temperature =  Math.round((94-32) * (5/9)) + ' centigrade'; //centigrade or celsius
      let newStory3 = newStory2
      .replaceAll('94 fahrenheit', temperature)
      .replaceAll('300 pounds', weight);
      story.textContent = newStory3;
      
    }
    else{
      let newStory3 = newStory2;
      story.textContent = newStory3;

    }
  }

  

  
  story.style.visibility = 'visible';
}