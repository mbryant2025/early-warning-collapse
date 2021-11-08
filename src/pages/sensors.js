import React from "react";
import './page.css'

const state1 = { status: false }
const state2 = { status: true }
const state3 = { status: true }
const state4 = { status: false }
const state5 = { status: true }

  
   function formatStatus(state){
    const {status} = state;
    return status === true ? 'Active' : 'Inactive';
  }
  function formatColor(state){
    const {status} = state;
    return status === true ? 'green-text' : 'red-text';
  }


const Sensors = () => {
    return (
        <div className = "page-styles">
            <div>
                <h1>Sensors Diagnostics:</h1>
                <span className= "bold-text">Sensor 1: </span>
                <span className= {formatColor(state1)}>{formatStatus(state1)}</span>
                <br></br>
                <span className= "bold-text">Sensor 2: </span>
                <span className= {formatColor(state2)}>{formatStatus(state2)}</span>
                <br></br>
                <span className= "bold-text">Sensor 3: </span>
                <span className= {formatColor(state3)}>{formatStatus(state3)}</span>
                <br></br>
                <span className= "bold-text">Sensor 4: </span>
                <span className= {formatColor(state4)}>{formatStatus(state4)}</span>
                <br></br>
                <span className= "bold-text">Sensor 5: </span>
                <span className= {formatColor(state5)}>{formatStatus(state5)}</span>
            </div>
            <div>
                <h2>[insert sensor map]</h2>
            </div>
        </div>
    );
};

export default Sensors;
