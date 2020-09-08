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

            $('.lead').text(lesson.name);
            $('.purpose').text(lesson.purpose);

            $('#tasks').append("<ul id='lessonTaskList'></ul>");
            for (let cnt = 0; cnt < task_lesson.length; cnt++) {
                $("#lessonTaskList").append("<li>" + task_lesson[cnt].name + ":" + task_lesson[cnt].description + "</li>");
            }
        }).catch((error) => {});
    });
}