import React, { Component } from 'react';
import { Spinner } from '../UI';

class LoginForm extends Component {

    state = {
        username: '',
        password: '',
        submitted: false,
        loading: false
    };

    handleChange = (e) => this.setState({ [e.target.name]: e.target.value });

    handleSubmit = (e) => {
        e.preventDefault();
        const { username, password } = this.state;
        this.setState({ submitted: true });
        this.setState({ loading: true });

        if (username && password) {
            this.props.login(username, password);
            this.setState({ loading: false });
        } else {
            this.setState({ loading: false });
        }
    }

    render() {
        const { username, password, submitted, loading } = this.state;

        if (loading) {
            return <Spinner />
        }

        return (
            <div className="container">
                <form name="text-center border border-light p-5" onSubmit={this.handleSubmit}>
                    <h2 className="h4 mb-4">Авторизация</h2>

                    <div className="form-group">
                        <label htmlFor="username">Логин</label>

                        <input
                            type="text"
                            className={"form-control" +  (submitted && !username ? " is-invalid" : "")}
                            name="username"
                            value={username}
                            onChange={this.handleChange}
                        />

                        { submitted && !username && <div className="invalid-feedback">Логин обязательное поле</div> }
                    </div>

                    <div className="form-group">
                        <label htmlFor="password">Пароль</label>

                        <input
                            type="password"
                            className={"form-control" +  (submitted && !password ? " is-invalid" : "")}
                            name="password"
                            value={password}
                            onChange={this.handleChange}
                        />

                        { submitted && !password && <div className="invalid-feedback">Пароль обязательное поле</div> }
                    </div>

                    <button className="btn btn-info btn-block my-4" type="submit">Войти</button>
                </form>
            </div>
        );
    }
}

export default LoginForm;