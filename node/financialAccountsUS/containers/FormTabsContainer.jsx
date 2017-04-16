import React from 'react'
import F1Form from './F1Form.jsx'
import { connect } from 'react-redux'
import { selectTab } from '../actions'
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs'

class FormTabsContainer extends React.Component {

    selectTab(index) {
        this.props.dispatch(selectTab(index))
    }

    render() {
        let tabs = this.props.tabs.map(tab => {
            return (
                <Tab>
                    {tab.name}
                </Tab>
                )
        })

        let panels = [
            <TabPanel>
                <F1Form key='F1Form'>
                </F1Form>
            </TabPanel>,
        ]
        return (
            <Tabs onSelect={this.selectTab.bind(this)}
                    selectedIndex={this.props.active}>
                <TabList>
                    {tabs}
                </TabList>
                {panels}
            </Tabs>
            )
    }
}

FormTabsContainer.PropTypes = {
    tabs: React.PropTypes.array.isRequired,
    active: React.PropTypes.number.isRequired
}

const mapStateToProps = state => {
    return {
        tabs: state.tabs.tabs,
        active: state.tabs.active
    }
}

export default connect(mapDispatchToProps)(FormTabsContainer)


