import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Redirect } from "react-router-dom";
import { logout, userData } from '../../actions/authAction';
import { isEmpty, getRandomBtnColor, getCurrentUser } from '../../utils';
import './style.css';


class ProfilePage extends Component {
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

        if (isEmpty(currentUser)) {
            return <Redirect to='/' />
        }

        return (
            <div className='container'>
                <section>
                    <div className="row mt-5">

                        <div className="col-lg-4 col-md-12">
                            <section className="card profile-card mb-4 text-center">
                                <div className="avatar z-depth-1-half">
                                    <img src="https://i.pravatar.cc/228" alt="" className="img-fluid" />
                                </div>
                            
                                <div className="card-body">
                                    <h4 className="card-title"><strong>{currentUser.first_name} {currentUser.last_name}</strong></h4>
                                    <h5>Квалификация: {currentUser.profile.qualification}</h5>
                                    <p className="dark-grey-text">{currentUser.profile.location}</p>
                                </div>
                            </section>
                            
                        </div>
                        
                        <div className='col-lg-8 col-md-12'>
                            <section className="card mb-4">
                                <div className="card-body text-center">
                                    <h5><strong>Навыки</strong></h5>

                                    <hr className="my-3" />

                                    {
                                        currentUser.profile.skills.map(skill => {
                                            const btnColorClass = getRandomBtnColor();
                                            const btnClass = `btn ${btnColorClass} btn-rounded btn-sm px-3 waves-effect waves-light`;
                                            return <button type="button" className={btnClass}>{skill}</button>
                                        })
                                    }                                   
                                </div>
                            </section>
                        </div>
                    </div>
                </section>
            </div>
        );
    }
}

const mapStateToProps = ({auth: { user }}) => {
    return { user }
};

const mapDispatchToProps = {
    logout,
    userData
};

export default connect(mapStateToProps, mapDispatchToProps)(ProfilePage);