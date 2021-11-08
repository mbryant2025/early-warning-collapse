import React from "react";
import './page.css'



const state = {status: 3 }

function formatStatus(){
    const {status} = state;
    if (status===1) {return 'Online'}
    else if (status===2) {return 'Inactive'}
    return 'On Alert';
  }

  function formatColor(){
    const {status} = state;
    return status === 1 ? 'green-text' : 'red-text';
  }



  function formatExplanation(){
    const {status} = state;
    if (status===1) {return <><p>
        The alert system is running properly
        </p></>}
        
    else if (status===2) {return <><p>
        The alert system is turned off. 
        The system will not set off in case of emergency.  
        </p></>}
    return <><p>
        The system is currently going off. Emergency State.
    </p></>
  }

const Alert = () => {
    return (
        <div className = "page-styles">
            <h1>Alert System</h1>
            <div>
                <span className= "bold-text">Current Alert Status: </span>
                <span className= {formatColor()}>{formatStatus()}</span>
                <br></br>
                <span  className = "explanation-text">{formatExplanation()}</span>
            </div>


            <div 
            style = {{
                display:'flex',
                justifyContent: 'center', 
                alignItems:'center',
                marginBottom: '4rem', 
            }}>
                <button className="button">
                    Overide System
                </button> 
            </div>



        </div>
    );
};

export default Alert;