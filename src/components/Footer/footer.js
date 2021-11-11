import React from "react";
import './footer.css'


function Footer() {
  return (
    <footer className = "page-styles" style={{margin:'15rem', alignContent:'center'}}> 
      <div>
    
        <img className= "logo" src="./images/EWS-logo.png" alt="./images/EWS-logo.png" />
        <span>&nbsp; This Project is Sponsored by Duke's EGR101 Class</span>
      

      </div>
    </footer>
    
  );
}

export default Footer;

