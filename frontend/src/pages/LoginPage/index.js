import React, { Component } from 'react';
import { connect } from 'react-redux';
import { login, userData } from '../../actions/authAction';
import LoginForm from '../../components/LoginForm';
import { Card, CardBody, CardHeader, CardImage } from '../../components/UI';
import {getCurrentUser, isEmpty} from "../../utils";

class LoginPage extends Component {
    state = {
        sessionUser: getCurrentUser()
    }

    componentDidMount() {
        const { user, token } = this.props;
        if (token && isEmpty(user) && isEmpty(this.state.sessionUser)) {
            this.props.userData();
        }
    }

    componentWillReceiveProps(nextProps){
        if (this.props.token !== nextProps.token) {
            this.props.userData();
        }
    }

    render() {
        const { user, login } = this.props;
        const { sessionUser } = this.state;

        if (!isEmpty(user) || !isEmpty(sessionUser)) {
            return <Card>
                <CardImage />

                <CardBody>
                    <CardHeader name='Вы авторизованы!' />

                </CardBody>
            </Card>
        }

        return (
            <div className='container'>

                <LoginForm login={login} />
            </div>
        );
    }
}


const mapStateToProps = ({ auth: { token, user, isLoggedIn } }) => {
    return { token, user, isLoggedIn }
}

const mapDispatchToProps = {
    login,
    userData
}

export default connect(mapStateToProps, mapDispatchToProps)(LoginPage);