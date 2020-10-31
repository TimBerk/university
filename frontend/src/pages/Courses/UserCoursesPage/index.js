import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Redirect } from 'react-router-dom';
import { getCourses } from '../../../actions/userAction';
import { CourseList } from '../../../components/Course';
import { Spinner, Card, CardBody, CardHeader, CardImage, CardLink } from '../../../components/UI';
import { isEmpty, getCurrentUser } from '../../../utils';


class UserCoursesPage extends Component {
    state = {
        sessionUser: getCurrentUser()
    }

    componentDidMount() {
        this.props.getCourses();
    }

    render() {
        const { user, courses } = this.props;
        const { sessionUser } = this.state;
        const currentUser = (isEmpty(user) && !isEmpty(sessionUser)) ? sessionUser : user;

        if (isEmpty(currentUser)) {
            return <Redirect to='/' />;
        }

        if (courses === undefined || courses === null) {
            return <Spinner />
        }
        
        if (courses.length === 0) {
            return <Card>
            <CardImage />

            <CardBody>
                <CardHeader name='Курсы не найдены' />
                <CardLink name='Записаться на курсы' link='/' />
            </CardBody>
        </Card>
        }

        return (
            <div className='container'>
                <CourseList items={courses} name='Список моих курсов' />
            </div>
        );
    }
}


const mapStateToProps = ({ user: { courses }, auth: { user }}) => {
    return { courses, user }
}

const mapDispatchToProps = {
    getCourses
}

export default connect(mapStateToProps, mapDispatchToProps)(UserCoursesPage)