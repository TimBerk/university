import { GET_USER_COURSE, REFRESH_TOKEN, JOIN_TO_COURSE } from "../constants/ActionTypes";
import { mainAxios, bearerHeader, refreshHeader, getToken } from '../utils';

const getUserCourse = results => ({type: GET_USER_COURSE, payload: results});

export const getRefreshToken = () => dispatch => {
    mainAxios.post(`auth/jwt/refresh/`,  refreshHeader())
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
        .then(response => dispatch(getUserCourse(response.data.results)))
        .catch(errors => {
            console.log(errors);

            if (errors.response.status === 401) {
                dispatch(getRefreshToken());
            }
        });
}

export const joinToCourse = (id) => dispatch => {
    const token = getToken();
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