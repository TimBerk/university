import React from 'react';
import moment from 'moment';
import { Link } from 'react-router-dom';
import { Modal } from '../UI'

const ScheduleModal = ({ modal, lesson, onClose }) => {
    const start = moment(lesson.start).locale("ru").format('D MMMM YYYY, h:mm');
    const end = moment(lesson.end).locale("ru").format('D MMMM YYYY, h:mm');

    return <Modal id='modalSchedule' show={modal} header='Лекция' onClose={onClose}>
        <ul className="list-group list-group-flush">
            <li className="list-group-item">
                <i className="fas fa-chalkboard"></i> <strong>{lesson.title}</strong>
            </li>

            <li className="list-group-item">
                <i className="fas fa-user-friends"></i> Группа {lesson.groupId}
            </li>

            <li className="list-group-item">
                <i className="fas fa-clock"></i> Начало занятия:<br/>{start}
            </li>

            <li className="list-group-item">
                <i className="fas fa-clock"></i> Конец занятия:<br/>{end}
            </li>

            <li className="list-group-item">
                <Link to={lesson.url} >
                    <i className="fas fa-link"></i> Ссылка на курс
                </Link>
            </li>
        </ul>
    </Modal>;
}

export default ScheduleModal;