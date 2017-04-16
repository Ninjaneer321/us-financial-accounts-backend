import 'babel-polyfill'
import React from 'react'
import { render } from 'react-dom'
import { Provider } from 'react-redux'
import { createStore, applyMiddleware} from 'redux'
import thunkMiddleware from 'redux-thunk'
import createLogger from 'redux-logger'

import financialAccountUsReducer from './reducer'

let logger = createLogger()

let store = createStore(financialAccountUsReducer,
                        applyMiddleware(logger, thunkMiddleware))

let app = (
    <Provider store={store}>

    </Provider>
    )

render(app, document.getElementById('main'))