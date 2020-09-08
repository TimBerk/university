import axios from 'axios';
import {getCookie} from '../../tools/coockies';

export default () => {
    const csrfToken = getCookie('csrftoken');

    $('.js-btn-course').on('click', (e) => {
        const dataId = $(e.currentTarget).data('id');

        axios({
            method: 'get',
            url: '/api/courses/lessons/detail/' + dataId,
            headers: {"X-CSRFToken": csrfToken},
        }).then((response) => {
            let lesson = response.data;

            $('#lesson-name').text(lesson.name);
            $('#description').text(lesson.description);
            $('#purposes').text(lesson.purpose);

            if ( $("#lessonTaskList").length ) {
               $("#lessonTaskList").remove();
            }
            $('#tasks').append("<ul id='lessonTaskList'></ul>");
            for (let cnt = 0; cnt < lesson.task_lesson.length; cnt++) {
                let current_task = lesson.task_lesson[cnt];
                $('#lessonTaskList').append("<li>" + current_task.name + ":" + current_task.description + "</li>");
            }
            if ( lesson.task_lesson.length === 0) {
                $('#lessonTaskList').append("<li>Задач нет</li>");
            }
        }).catch((error) => {});
    });
}