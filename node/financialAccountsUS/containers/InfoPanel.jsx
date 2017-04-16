import { connect } from 'react-redux'
import { InfoPanel } from '../components/InfoPanel.jsx'


const mapStateToProps = state => {
    return {
        title: state.infoPanel.title,
        body: state.infoPanel.body
    }
}

export default connect(mapStateToProps)(InfoPanel)
