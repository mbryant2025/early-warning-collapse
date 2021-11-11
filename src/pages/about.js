import React from "react";
import './page.css'


const About = () => {
    return (
        <div style={{fontFamily: 'sans-serif', marginLeft:'10rem', marginRight: '10rem'}}>
            
            <img className = "front-image" src="./images/EWS-Banner.png" alt="./images/EWS-Banner.png" />
            <h1 
            style = {{
                display:'flex',
                justifyContent: 'center', 
                alignItems:'center',
                marginBottom: '4rem', 
                }}>
                About The Team  
            </h1>

            <h2 style={{fontWeight: 'bold',marginBottom:'1rem'}}>Hardware Team</h2>
            <div className= "about-text">
                <span>Tommy Jablonski—lead hardware developer</span>
                <ul>
                    <li>Created blah blah</li>
                </ul>
                <span>Lucy Huo</span>
                <ul>
                    <li>empty</li>
                </ul>
                <span>Shun Sakai</span>
                <ul>
                    <li>empty</li>
                </ul>
                <span>I forgot Sorry</span>
                <ul>
                    <li>empty</li>
                </ul>
            </div>

            <h3 style={{fontWeight: 'bold',marginBottom:'1rem'}}>Software Team</h3>
            <div className= "about-text">
                <span>Brayden Hand—Software Team Lead</span>
                <ul>
                    <li>Developed graphical interpolation algorithms for real-time data.</li>
                </ul>
                <span>Arnav Nayak—Lead Backend Developer</span>
                <ul>
                    <li>Created real-time database integrated with sensor mesh network.</li>
                </ul>
                <span>Michael Bryant—Software Engineer</span>
                <ul>
                    <li>Developed second order linear regression model used 
                        in the machine learning algorithm for collapse coefficients.</li>
                </ul>
                <span>Alvin Hong—Frontend Developer</span>
                <ul>
                    <li>Developed website for client and established direction for product.</li>
                </ul>
            </div>

            <h4 style={{fontWeight: 'bold',marginBottom:'1rem'}}>Contact/Links </h4>
            
            <span>Email us:&nbsp;<a href="mailto:brayden.hand@duke.edu">
                brayden.hand@duke.edu 
            </a></span>
            <span>, &nbsp;<a href="mailto:alvin.hong@duke.edu">
                alvin.hong@duke.edu
            </a></span>
            <span>, &nbsp;<a href="mailto:micheal.bryant@duke.edu">
                micheal.bryant@duke.edu
            </a></span>
            <span>, &nbsp;<a href="mailto:arnav.nayak@duke.edu">
                arnav.nayak@duke.edu
            </a></span>
                
            <br></br>
            <span>GitHub:&nbsp;<a href="https://github.com/rNuv/early-warning-collapse.git">
            GitHub-- Early Collapse Warning System
            </a></span>
            <br></br>
            <span>Website/Future Directions:&nbsp;<a href="https://sites.duke.edu/ewcd/vision/">
            About The Project
            </a></span>

        </div>
    );
};

export default About;
