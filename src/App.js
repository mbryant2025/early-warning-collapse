import React from 'react';
import './App.css';
import Navbar from "./components/Navbar/Navbar";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Home from './pages';
import About from './pages/about';
import Readings from './pages/readings.js';
import Sensors from './pages/sensors';
import Alert from './pages/alert';
import Footer from './components/Footer/footer';


function App() {
  return (
  
    <div className="App py container -m">
       <Router>
        <Navbar/>
        <Switch>
          <Route path= '/' exact component = {Home} />
          <Route path= '/sensors' exact component = {Sensors} />
          <Route path= '/readings' exact component = {Readings} />
          <Route path= '/alert' exact component = {Alert} />
          <Route path= '/about' exact component = {About} />
        </Switch>
        <Footer/>
      </Router>

    </div>
  );
}

export default App;
