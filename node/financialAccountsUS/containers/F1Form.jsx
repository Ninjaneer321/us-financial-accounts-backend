import React from 'react'
import db from '../db'
import { connect } from 'react-redux'
import {
    f1Form_selectSymbol, f1Form_selectTable,
    f1Form_setData, plotF1Form,
} from '../actions'


class F1Form extends React.Components {
    constructor(props) {
        super(props)
        this.state = {
            tablesWaiting: true,
            tables: [],
            symbols: []
        }

        db.getAllTableCodes().then(tables => {
            this.setState({
                tables: tables,
                tablesWaiting: false
            })
        })
    }

    tableSelected(event) {
        let dispatch = this.props.dispatch
        dispatch(f1Form_selectTable(parseInt(event.target.value)))
    }

    symbolSelected(event) {
        let dispatch = this.props.dispatch
        dispatch(f1Form_selectSymbol(parseInt(event.target.value)))
    }

    submit() {
        let dispatch = this.props.dispatch
        dispatch(platF1Form({
            table
        }))
    }

    render() {
        if (this.state.tablesWaiting) {
            return ( <div> waiting... </div> )
        }

        let tablesDropdownItems = this.state.tables.map(table => {
            return ( <option value={table.id}> {table.table_code} </option> )
        })
        let tablesDropdown = ( 
            <select value={this.props.tableId || undefined}
                    onChange={this.tableSelected.bind(this)}>
                {tablesDropdownItems} 
            </select> 
            )

        let symbolsDropdownItems = this.state.symbols.map(symbol => {
            return ( <option value={symbol.id}> {symbol.symbol} </option> )
        })
        let symbolsDropdown = ( 
            <select value={this.props.symbolId || undefined} 
                    onChange={this.symbolSelected.bind(this)}>
                {symbolsDropdownItems} 
            </select> 
            )

        return (
            <div>
                <div> tablesDropdown </div>
                <div> symbolsDropdown </div>
                <div> 
                    <button onClick={this.submit.bind(this)}>
                    Plot
                    </button>
                </div>
            </div>
            )
    }
}

F1Form.PropTypes = {
    tableId: react.PropTypes.number.isRequired,
    symbolId: react.PropTypes.number.isRequired,
    dispatch: react.PropTypes.func.isRequired
}

const mapStateToProps = state => {
    return {
        tableId: state.forms.f1Form.tableId,
        symbolId: state.forms.f1Form.symbolId
    }
}

export default connect(mapStateToProps)(F1Form)




