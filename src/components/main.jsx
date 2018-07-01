import React from 'react'
import './main.sass' //import component style

class Main extends React.Component{
	constructor(props) {
		super(props)
	}
	render() {
		return (
			<div id="main-container">
				<h1>Hello, flask-react</h1>
			</div>
		)
	}
}

export default Main