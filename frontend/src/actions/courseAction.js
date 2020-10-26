import { GET_COURSE_LIST, GET_COURSE } from "../constants/ActionTypes";
import { mainAxios } from '../utils';


export const getCourseList = () => dispatch => {
    mainAxios.get('courses/')
        .then(res => {
            dispatch({
                type: GET_COURSE_LIST,
                payload: res.data.results
            })
        })
        .catch((err) => console.log(err));
}

export const getCourse = (id) => dispatch => {
    mainAxios.get(`courses/${id}/`)
        .then(res => {
            dispatch({
                type: GET_COURSE,
                payload: res.data
            })
        })
        .catch((err) => console.log(err));
}