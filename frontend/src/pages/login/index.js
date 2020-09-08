import axios from 'axios';
import { getCookie } from '../../tools/coockies';

export default () => {
    const $form = $('.js-login-form');
    const csrfToken = getCookie('csrftoken');

    $form.submit( function(event) {
        event.preventDefault();

        let username = $('#id_username').val();
        let password = $('#id_password').val();

        axios({
            method: 'post',
            url: '/api/user/login',
            data: {
                username: username,
                password: password
            },
            headers: {"X-CSRFToken": csrfToken},
        }).then((response) => {
            let token = response.data.auth_token;
            window.localStorage.setItem('token', token);
            window.location.href = "/";
        }).catch((error) => {
            window.location = "/student/login";
            console.log('Error on Authentication');
        });
    });
}