import React from 'react'

class InfoPanel extends React.Component {
    render() {
        let title = this.props.title,
            body = this.props.body;
        return (
            <div>
                <div>
                    {title}
                </div>

                <div>
                    {body}
                </div>
            </div>
            )
    }
}

InfoPanel.PropTypes = {
    title: React.PropTypes.string.isRequired,
    body: React.PropTypes.string.isRequired
}

export default InfoPanel