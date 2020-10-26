import axios from "axios";
import Cookies from 'universal-cookie';
import { GET_CSRF_TOKEN } from '../constants/ActionTypes'
const BASE_URL = 'http://localhost:8000/api/';

export const mainAxios = axios.create({
    baseURL: BASE_URL,
});

export const csrfAxios = (csrfToken) => {
    return axios.create({
        baseURL: BASE_URL,
        xsrfHeaderName: "X-CSRFToken",
        xsrfCookieName :"csrftoken",
        withCredentials: true,
        headers: {
            "X-CSRFToken": csrfToken,
        }
    });
}

export const bearerHeader = () => {
    const token = localStorage.getItem('token')

    if (token) {
        return {
            headers: { Authorization: ` Bearer ${token}` }
        }
    } else {
        return {}
    }
};

export const refreshToken = () => {
    const token = localStorage.getItem('refresh_token')

    if (token) {
        return { refresh: token }
    } else {
        return {}
    }
};

export const checkOrSetCsrfToken = () => dispatch => {
    const cookies = new Cookies();
    const csrfToken = cookies.get('csrftoken');

    if (csrfToken === undefined) {
        mainAxios
        .post("user/session-token/")
        .then((response) => {
            if (response.data.csrf_token) {
                cookies.set('csrftoken', response.data.csrf_token)
                return dispatch({
                    type: GET_CSRF_TOKEN
                })
            }
    
        })
        .catch((err) => console.log(err));
    }
}