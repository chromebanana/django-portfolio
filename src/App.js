import React, { Component } from 'react';
import { Navigation } from './Navigation';
import { BrowserRouter as Router } from 'react-router-dom';
import BaseRouter from './routes';

import './App.css';

class App extends Component {
  constructor() {
      super();
      this.state = {
        route: 'home'
      }
  }

  onRouteChange = (route) => {
    this.setState({route: route})
  }

  render() {
    const { route } = this.state;
 // TODO: https://en.wikipedia.org/wiki/Centrifugal_governor
  return (
    <div className="App mw7 w-90 ph3 pv4-l pv4-m center">
        <Router> 
          <Navigation onRouteChange={this.onRouteChange}/>

          <BaseRouter/>
        </Router>
    
  </div>
  );
}
}

export default App;
