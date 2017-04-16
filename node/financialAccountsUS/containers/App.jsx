import React from 'react'
import FormTabsContainer from './FormTabsContainer.jsx'
import Graph from './Graph.jsx'
import InfoPanel from './InfoPanel.jsx'

class App extends React.Component {
    render() {
        return (
            <div>
                <FormTabsContainer>
                </FormTabsContainer>

                <InfoPanel>
                </InfoPanel>

                <Graph>
                </Graph>
            </div>
            )
    }
}


export default App
