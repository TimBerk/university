import axios from "axios";
import { GET_CSRF_TOKEN } from '../constants/ActionTypes'
import {getToken, getRefreshToken, getCsrfToken, cookies} from "./storages";

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
    const token = getToken();
    return token ? { headers: { Authorization: ` Bearer ${token}` } } : {};
};

export const refreshHeader = () => {
    const token = getRefreshToken();
    return token ? { refresh: token } : {};
};

export const checkOrSetCsrfToken = () => dispatch => {
    const csrfToken = getCsrfToken()

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