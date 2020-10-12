import React from 'react';
import { Route } from 'react-router-dom';

import Home from './Home';
import About from './About';
import Portfolio from './Portfolio';
import { Contact } from './Contact';

const BaseRouter = () => (
	<div>
		<Route exact path='/' component={Home} />
		<Route exact path='/about' component={About} />
		<Route exact path='/portfolio' component={Portfolio} />
		<Route exact path='/contact' component={Contact} />
	</div>
)

export default BaseRouter;