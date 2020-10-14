import React from 'react';
import axios from 'axios';
import Button from '../components/Button.js'

const PortfolioItem = ({ date, role, title, location, detail, body }) => {
  return (
  		<div className="pv2">
  		<article className="ba ph4 pv2">
		<h3>{date}</h3>
		<h3>{role}</h3>
		<h2>{title}</h2>
		<h3>{location}</h3>
		<h4>{detail}</h4>
		{body}
		</article>	
  		</div>
    )
}

class Portfolio extends React.Component {
	constructor() {
		super();
		this.state = {
			category: 'Professional',
            articlesData: []
		}
	}

    componentDidMount() {
        axios.get('/api/')
        .then(res => {
            this.setState({
                articlesData: res.data
            })
        })
    }

	changePortfolioCategory = (event) => {
		let target = event.target
		this.setState({category: target.text})

	}

 render() {
    var articles = this.state.articlesData

 	return (
          <div>
           { 
            Object.keys(articles).map((type, i) => { 
                return ( <Button key={i}
                                text={type} 
                                active={this.state.category===type} 
                                onClick={this.changePortfolioCategory}/>
                                )
            })
            }

            {Object.keys(articles).map((article) => { 
                return ( 
                    articles[article].map((field, i) => {
                        if(this.state.category === article) 
                        { return (
                             <PortfolioItem key={i}
                                date={field.date} 
                                role={field.role}
                                title={field.title} 
                                location={field.location} 
                                body={field.body}/>
                            )}
                    })
            )
                
                })}
        </div>
        );
    } 
}

export default Portfolio;