import { LOGIN_REQUEST, LOGOUT_REQUEST, GET_USER_DATA } from "../constants/ActionTypes";
import { mainAxios, bearerHeader } from '../utils';


export const login = (username, password) => (dispatch) => {

    return mainAxios
        .post("auth/jwt/create/", {
            username,
            password,
        })
        .then((response) => {
            const token = response.data;

            if (token) {
                localStorage.setItem("token", token.access);
                localStorage.setItem("refresh_token", token.refresh);

                return dispatch({
                    type: LOGIN_REQUEST,
                    payload: token.access,
                    refresh_token: token.refresh
                });
            }
        })
        .catch((err) => console.log(err));
};


export const userData = () => (dispatch) => {
    return mainAxios
        .get("user/", bearerHeader())
        .then((response) => {
            if (response) {
                sessionStorage.setItem('userData', JSON.stringify(response.data));

                return dispatch({
                    type: GET_USER_DATA,
                    payload: response.data
                });
            }
        })
        .catch((err) => console.log(err));
};


export const logout = () => (dispatch) => {
    return mainAxios
        .post("user/logout/", { token: localStorage.getItem('refresh_token') })
        .then(() => {
            localStorage.removeItem('token');
            localStorage.removeItem('refresh_token');
            sessionStorage.removeItem('userData');

            return dispatch({
                type: LOGOUT_REQUEST
            });
        })
        .catch((err) => console.log(err));
}

export const userActions = {
    login,
    logout
};