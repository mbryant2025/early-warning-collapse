import React from "react";
import { NavLink } from "react-router-dom";


const Navbar = () => {
    return(
        
        <Nav>
            <NavLink to = "/">
                <h1>Logo</h1>
            </NavLink>
            <NavMenu>
                <NavLink to="/sensors.js" activeStyle>
                    Sensors
                </NavLink>
                <NavLink to="/readings.js" activeStyle>
                    Readings
                </NavLink>
                <NavLink to="/alert.js" activeStyle>
                    Alert
                </NavLink>
                <NavLink to="/about.js" activeStyle>
                    About
                </NavLink>
            </NavMenu>
        </Nav>
    )
}
