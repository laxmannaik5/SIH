import React from 'react';
import Rectangle from '../image/rectangle.svg';
import Frame from '../image/frame.svg';

function Card(){
    return(
        <div className="card">
          <div className="card-body">
            <div className="container card1">
            <div class="row">
                    <div class="column rectangle">
                        <img className='image' src={Rectangle}></img>
                    </div>
                    <div class="column text">
                        <h4><b>Normal</b></h4> 
                        <p>No threat near the ocean</p>
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
                        <p>32km/hr</p>
                    </div>
                    <div class="column">
                        <h4><b>Intensity</b></h4> 
                        <p>Normal</p>
                    </div>
                    <div class="column">
                        <h4><b>See More</b></h4> 
                        <p>+</p>
                    </div>
                </div>
            </div>
          </div>
            
        </div>
    );
}
export default Card;