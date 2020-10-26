import React, { Component } from 'react';
import { connect } from 'react-redux';
import { getCourseList } from '../../actions/courseAction';
import { CourseList } from '../../components/Course';

class MainPage extends Component {
    state = {
        courses: []
    }
    componentDidMount() {
        this.props.getCourseList();
    }

    componentWillReceiveProps(props) {
        if (props.courses) {
            this.setState({
                courses: props.courses
            })
        }
    }

    getLessonInfo = (id) => {

    }

    render() {
        const { courses } = this.state;

        return (
            <div className='container'>

                <CourseList items={courses} />
            </div>
        );
    }
}


const mapStateToProps = ({ courses: { items } }) => {
    return { courses: items }
}

const mapDispatchToProps = {
    getCourseList
}

export default connect(mapStateToProps, mapDispatchToProps)(MainPage)