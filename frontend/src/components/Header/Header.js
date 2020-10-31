import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Link } from "react-router-dom";
import { logout, userData } from '../../actions/authAction';
import { isEmpty, getCurrentUser } from '../../utils';

import HeaderUser from './HeaderUser';

class Header extends Component {
    state = {
        sessionUser: getCurrentUser()
    }

    componentDidMount() {
        const { user, token } = this.props;
        if (token && isEmpty(user) && isEmpty(this.state.sessionUser)) {
            this.props.userData();
        }
    }

    logoutAccount = e => {
        e.preventDefault();
        this.props.logout();
    };

    render() {
        const { user } = this.props;
        const { sessionUser } = this.state;
        const currentUser = (isEmpty(user) && !isEmpty(sessionUser)) ? sessionUser : user;

        const loginLink = (!isEmpty(user) || !isEmpty(sessionUser)) ? null : <li className="nav-item"><Link className="nav-link" to="/login">Войти</Link></li>;

        return (
            <nav className="mb-1 navbar navbar-expand-lg navbar-dark default-color">
                <Link className="navbar-brand" to="/">University</Link>
                <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbar"
                        aria-controls="navbar" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbar">
                    <ul className="navbar-nav mr-auto">
                        <li className="nav-item">
                            <Link className="nav-link" to="/schedule/">Расписание
                            </Link>
                        </li>
                        { loginLink }
                    </ul>

                    <HeaderUser user={currentUser} logout={this.logoutAccount}/>
                </div>
            </nav>
        );
    }
}

const mapStateToProps = ({auth: { user, isLoggedIn }}) => {
    return { user, isLoggedIn }
};

const mapDispatchToProps = {
    logout,
    userData
};

export default connect(mapStateToProps, mapDispatchToProps)(Header);