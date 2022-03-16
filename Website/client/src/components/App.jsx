import React, {useState} from 'react';
import NormalCard from './NormalCard';
import DangerCard from './DangerCard';
import FooterCard from './FooterCard';

function App(){

    const [isDone, setIsDone] = useState(false);

    function handleClick(){
        setIsDone(!isDone);
    }

    return(
        <div onClick={handleClick}>

            {!isDone ? <NormalCard /> : <DangerCard />}
            
            <FooterCard />

        </div>
    );
}
export default App;