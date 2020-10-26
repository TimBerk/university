import { GET_USER_COURSE, REFRESH_TOKEN, JOIN_TO_COURSE } from "../constants/ActionTypes";
import { mainAxios, bearerHeader, refreshToken } from '../utils';

export const getRefreshToken = () => dispatch => {
    mainAxios.post(`auth/jwt/refresh/`,  refreshToken())
    .then(response => {
        localStorage.setItem("token", response.data.access);

        return dispatch({
            type: REFRESH_TOKEN,
            payload: response.data.access
        });
    })
    .catch((err) => console.log(err));
}

export const getCourses = () => dispatch => {
    mainAxios.get(`user/courses/`,  bearerHeader())
        .then(response => {

            return dispatch({
                type: GET_USER_COURSE,
                payload: response.data.results
            })
        })
        .catch(errors => {
            console.log(errors);

            if (errors.response.status === 401) {
                dispatch(getRefreshToken());
            }
        });
}

export const joinToCourse = (id) => dispatch => {
    const token = localStorage.getItem('token')
    mainAxios.defaults.headers.common['Authorization'] = ` Bearer ${token}`;

    mainAxios.post(`user/join-to-course/${id}/`)
        .then(response => {

            return dispatch({
                type: JOIN_TO_COURSE,
                payload: response.data.results
            })
        })
        .catch(errors => {
            console.log(errors);

            if (errors.response.status === 401) {
                dispatch(getRefreshToken());
            }
        });
}