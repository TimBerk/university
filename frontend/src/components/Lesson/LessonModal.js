import React from 'react';
import { Modal } from '../UI'

const LessonModal = ({ id, modal, lesson, onClose }) => {
    return <Modal id={id} show={modal} header={lesson.name} onClose={onClose}>
        <div className="text-center">
            <i className="far fa-file-alt fa-4x mb-3 animated rotateIn"></i>
            <p className="text-center">
                <strong>Описание</strong>
            </p>
            <p>{lesson.description}</p>
        </div>

        <hr />

        <div className="text-center">
            <p className="text-center">
                <strong>Цели</strong>
            </p>
            {lesson.description}

            <hr />

            <p className="text-center">
                <strong>Задачи</strong>
            </p>

            <ul className="text-left">
                {
                    lesson.task_lesson.map((task) => {
                        return <li key={task.id}>{task.name}</li>
                    })
                }
            </ul>
        </div>
    </Modal>;
}

export default LessonModal;