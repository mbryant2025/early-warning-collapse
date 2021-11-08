import React from "react";
import logo from './pages/images/EWS-logo.png';
import './pages/page.css'


function Footer() {
  return (
    <div className = "page-styles" style={{margin:'15rem', alignContent:'center'}}>
    
      <img className= "logo" src={logo} alt="logo" />
      <span>&nbsp; This Project is Sponsored by Duke's EGR 101 Class</span>
      

    </div>
  );
}

export default Footer;
