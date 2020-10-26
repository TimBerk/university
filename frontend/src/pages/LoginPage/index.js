import React, { Component } from 'react';
import { connect } from 'react-redux';
import { login, userData } from '../../actions/authAction';
import LoginForm from '../../components/LoginForm';
import { Card, CardBody, CardHeader, CardImage } from '../../components/UI';

class LoginPage extends Component {
    componentWillReceiveProps(nextProps){
        if (this.props.token !== nextProps.token) {
            this.props.userData();
        }
    }

    render() {
        const { user, login } = this.props;

        if (Object.keys(user).length > 0) {
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