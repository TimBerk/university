import React, { Component, Fragment } from 'react';
import { Link } from "react-router-dom";

const LessonList = ({ items, loadLesson }) => {
    if (items.length < 1) {
        return <h3>Лекции пока нет</h3>
    }

    return (
        <Fragment>
            <h3>Список лекций:</h3>

            <ul className="list-group list-group-flush">
            {
                items
                    .map((lesson) => {
                    return <li className="list-group-item" key={lesson.id}>
                        {lesson.name}
                        <span className="badge badge-primary badge-pill js-btn-course ml-2"
                              data-toggle="modal"
                              onClick={(e) => loadLesson(lesson.id)}
                        >
                            Подробнее
                        </span>
                    </li>
                })
            }
            </ul>
        </Fragment>
    );
}

class CourseDetail extends Component {

    render() {
        const { currentCourse, loadLesson, joinToCourse, canJoin=false } = this.props;
        const btnJoin = canJoin ? <button onClick={() => joinToCourse(currentCourse.id)} className="btn btn-primary btn-sm">Поступить на курс</button> : null;

        return <div className="container">
            <h1 className="text-center mt-5 mb-2">{currentCourse.name}</h1>

            <blockquote className="blockquote">
                <div dangerouslySetInnerHTML={{ __html: currentCourse.description }} />

                <Link to="/" className="btn btn-primary btn-sm">Вернуться</Link>
                { btnJoin }
            </blockquote>

            <LessonList items={currentCourse.lessons} loadLesson={loadLesson} />
        </div>
    }
}

export default CourseDetail;