import React from 'react';
import Rectangle from '../image/danger-rectangle.svg';
import Frame from '../image/danger-frame.svg';

function DangerCard(){
    return(
        <div className="card">
          <div className="card-body">
            <div className="container card1">
            <div class="row">
                    <div class="column rectangle">
                        <img className='image' src={Rectangle}></img>
                    </div>
                    <div class="column text">
                        <h4><b>Danger</b></h4> 
                        <p>Threat is there near the ocean</p>
                    </div>
                    <div class="column frame">
                        <img className='image' src={Frame}></img>
                    </div>
                </div>
            </div>
          </div>
          <div className="card-body">
            <div className="container card2"> 
                <div class="row">
                    <div class="column">
                        <h4><b>Wind Speed</b></h4> 
                        <p>132km/hr</p>
                    </div>
                    <div class="column">
                        <h4><b>Intensity</b></h4> 
                        <p>Danger</p>
                    </div>
                    <div class="column">
                        <h4><b>See More</b></h4> 
                        <p><b>+</b></p>
                    </div>
                </div>
            </div>
          </div>
            
        </div>
    );
}
export default DangerCard;