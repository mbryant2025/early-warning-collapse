//import building from './images/homepage-image.png';
import building from './images/surfside-building-collapse-pic.jpg';
import React from 'react';
import './page.css'

//this is to change the status displayed (true=safe; false=needs inspection)
 const state = {
  result: true
 }

 function formatWarning(){
  const {result} = state;
  return result === true ? 'Safe System' : 'Needs Maintenance';
}
function formatWarningColor(){
  const {result} = state;
  return result === true ? 'green-text' : 'red-text';
}

function formatExplanation(){
  const {result} = state;
  if (result===true) {return <><p>
      Safe System: Sensors indicate a safe building with normal readings. No current action
      needed.
      </p></>}

  return <><p>
      Needs Maintenace: The system has shown some 
      level of concern regarding sensor data. For maximum safety, the building structure
      should be examined for irregularities.  
      </p></>
}

const Home = () => {
  
  
  return (  
      <div className = "page-styles">
        <img className = "front-image" src={building} alt="building" />

        <p className = "basic-text" style={{marginTop:'2rem'}}>
        The Early Warning Collapse System strives to detect minute 
        changes in buildings to determine when a building is at risk of collapse. To do this, the system 
        will collect sensor data using sensors created by esp32 microcontrollers and running 
        an algorithm to detect irregularities. With that data, we hope to save lives by alerting 
        residents and building personel of any possible concerns. 
        This project is created by the EWS #1 Duke EGR 101 Team. 
        </p>
        <br></br>

        <span className = "bold-text"> Current Status: </span>
        <span className= {formatWarningColor()}>{formatWarning()}</span>
        <span>{formatExplanation()}</span>
        <br></br>
        

        <span className = "bold-text"> Overview: </span>
        <br></br>

        <div>
          <p className="basic-text"> 
          [insert daily graphs]~ [insert radar graph] 
          </p>
        </div>


      </div>  
      
  );
  
};


export default Home;
