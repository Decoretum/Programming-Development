import { useLocation } from "react-router-dom"

export default function Clue(props){
    const location = useLocation(); //access present state of child
    const data = location.state.data;
    console.log(data)
    let hooker = document.getElementById('bord');
    for (let i = 0; i < data.length; i++){
        //hooker.innerHTML += data[i];
    }
    console.log(data[0][''])
    return( 
        <>
            <h1> Category Number: {data[0]['num']}  </h1>
            <div id="bord" style={{border:'solid'}}> 
                
                {data.map((val, index) => {
                    return (
                        <div key={index}>
                            <p>{JSON.stringify(val)}</p>
                            <br></br>
                        </div>
                    )
                })}
            </div>
        
        </>
    )
}