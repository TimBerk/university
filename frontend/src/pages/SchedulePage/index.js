import React, { Component } from 'react';
import { connect } from 'react-redux';
import { getCalendar } from '../../actions/scheduleActions';
import { ScheduleCalendar, ScheduleModal } from '../../components/Schedule'

class SchedulePage extends Component {
    state = {
        lessons: [],
        lesson: null,
        modal: null
    }

    componentDidMount() {
        this.props.getCalendar();
    }

    componentWillReceiveProps(props) {
        if (props.lessons) {
            this.setState({
                lessons: props.lessons
            })
        }
    }

    renderLessonInfo = (lessonInfo) => {
        lessonInfo.jsEvent.preventDefault();

        this.setState({
            modal: !this.state.modal,
            lesson: lessonInfo.event
        })
    }
    
    closeLesson = () => {
        this.setState({
            modal: !this.state.modal,
            lesson: null
        })
    }

    render() {
        const { lessons, lesson, modal } = this.state;
        let lessonModal = null;

        if (modal && lesson) {
            lessonModal = <ScheduleModal modal={modal} lesson={lesson} onClose={this.closeLesson} />;
        }

        return (
            <div className='container'>

                <ScheduleCalendar
                    eventsSet={this.props.getCalendar}
                    eventContent={ this.renderLessonInfo }
                    events={lessons}
                />

                { lessonModal }
            </div>
        );
    }
}


const mapStateToProps = ({ schedule: { items } }) => {
    return { lessons: items }
}

const mapDispatchToProps = {
    getCalendar
}

export default connect(mapStateToProps, mapDispatchToProps)(SchedulePage)