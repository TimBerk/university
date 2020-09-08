import axios from 'axios';

export default () => {
    const $form = $('.js-login-form');
    const $submitButton = $('.submit-login-form');

    console.log($form);
    console.log($submitButton);

    $form.submit( function() {
        axios({
            method: 'post',
            url: '/api/simple-token/',
            data: {
                username: 'admin',
                password: 'admin'
            }
        }).then((response) => {
            console.log(response);
        }, (error) => {
            console.log(error);
        });
    });
}