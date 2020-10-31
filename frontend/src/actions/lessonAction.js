import { GET_LESSON } from "../constants/ActionTypes";
import { mainAxios } from '../utils';

export const getLesson = (id) => dispatch => {
    mainAxios.get(`courses/lessons/detail/${id}`)
        .then(res => {
            dispatch({
                type: GET_LESSON,
                payload: res.data
            })
        })
        .catch((err) => console.log(err));
}