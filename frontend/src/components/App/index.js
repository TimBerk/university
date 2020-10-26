import React, { Component, Fragment } from 'react';

import { Provider } from 'react-redux';
import store from "../../store";

import 'mdbootstrap/css/bootstrap.min.css';
import 'mdbootstrap/css/mdb.min.css';
import '@fortawesome/fontawesome-free/css/all.css'

import 'jquery/dist/jquery.min';
import 'popper.js/dist/popper.min';
import 'mdbootstrap/js/bootstrap.min';

import { AppRouter } from '../../pages';


class App extends Component {
    render() {
        return <Provider store={ store }>
            <AppRouter />
        </Provider>
    }
}

export default App;