import { parseJSON } from 'jquery';
import React, { Component, Fragment } from 'react';
import { CourseDetail } from '../../../components/Course';
import { connect } from 'react-redux';
import { getCourse } from '../../../actions/courseAction';
import { getLesson } from '../../../actions/lessonAction';
import { joinToCourse } from '../../../actions/userAction';
import { Spinner } from '../../../components/UI';
import { LessonModal } from '../../../components/Lesson';
import { isEmpty } from '../../../utils';


class CoursePage extends Component {
    state = {
        course: this.props.course,
        lesson: this.props.lesson,
        modal: false,
        sessionUser: sessionStorage.getItem('userData') ? parseJSON(sessionStorage.getItem('userData')) : {}
    };

    componentDidMount() {
        const { match } = this.props;
        const { id } = match.params;
        this.props.getCourse(id);
    }

    componentWillReceiveProps(nextProps){
        if(this.props.course !== nextProps.course && this.props.course !== undefined){
            this.setState({
                course: nextProps.course
            })
        }

        if(this.props.lesson !== nextProps.lesson && this.props.lesson !== undefined){
            this.setState({
                lesson: nextProps.lesson
            })
        }
    }

    joinToCourse = (id) => {
        this.props.joinToCourse(id);
    }

    loadLesson = (id) => {
        this.setState({
            modal: !this.state.modal
        });
        this.props.getLesson(id);
    }

    closeLesson = () => {
        this.setState({
            modal: !this.state.modal,
            lesson: null
        })
    }


    render() {
        const { course, lesson, modal, sessionUser } = this.state;
        const { user } = this.props;
        const canJoin = (isEmpty(user) && !isEmpty(sessionUser));

        let lessonModal = null;
        if (course === undefined || course === null) {
            return <Spinner />
        }

        if (modal && lesson) {
            lessonModal = <LessonModal id='modalLesson' modal={modal} lesson={lesson} onClose={this.closeLesson} />;
        }

        return (
            <Fragment>
                <CourseDetail currentCourse={course} loadLesson={this.loadLesson} joinToCourse={this.joinToCourse} canJoin={canJoin} />
                
                { lessonModal }
            </Fragment>
        );
    }
}


const mapStateToProps = ({ courses: { course }, lessons: {lesson}, auth: { user } }) => {
    return { course, lesson, user }
}

const mapDispatchToProps = {
    getCourse,
    getLesson,
    joinToCourse
}

export default connect(mapStateToProps, mapDispatchToProps)(CoursePage)