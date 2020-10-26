import React from 'react';
import { Link, Redirect } from 'react-router-dom';
import { isEmpty } from '../../utils';

const HeaderUser = ({ user, logout }) => {
    if (isEmpty(user)) {
        return <Redirect to='/'/>;
    }

    return (
    <ul className="navbar-nav ml-auto nav-flex-icons">
        <li className="nav-item dropdown">
            <a className="nav-link dropdown-toggle" id="navbarDropdownMenuLink-user" data-toggle="dropdown"
                aria-haspopup="true" aria-expanded="false">
                <i className="fas fa-user"></i> {user.username}
            </a>
            <div className="dropdown-menu dropdown-menu-left dropdown-default"
            aria-labelledby="navbarDropdownMenuLink-user">
                <Link to="/profile/" className="dropdown-item">Профиль</Link>
                <Link to="/my/courses" className="dropdown-item">Мои курсы</Link>
                <Link
                    to='#'
                    className="dropdown-item"
                    onClick={logout}
                >
                    Выйти
                </Link>
            </div>
        </li>
    </ul>
    );
}

export default HeaderUser;