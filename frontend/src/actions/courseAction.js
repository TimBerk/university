import {GET, REQUEST, SUCCESS, FAILURE, COURSE_LIST, COURSE} from "../constants/ActionTypes";
import { mainAxios } from '../utils';


const boundListRequest = () => ({ type: COURSE_LIST + "_" + GET + "_" + REQUEST});
const boundListSuccess = results => ({ type: COURSE_LIST + "_" + GET + "_" + SUCCESS, payload: results});
const boundListFailure = error => ({ type: COURSE_LIST + "_" + GET + "_" + FAILURE, payload: error});

export const getCourseList = () => dispatch => {
    dispatch(boundListRequest())
    return mainAxios.get('courses/')
        .then(res => dispatch(boundListSuccess(res.data.results)))
        .catch(err => dispatch(boundListFailure(err.response.statusText)));
}


const boundItemRequest = () => ({ type: COURSE + "_" + GET + "_" + REQUEST});
const boundItemSuccess = results => ({ type: COURSE + "_" + GET + "_" + SUCCESS, payload: results});
const boundItemFailure = error => ({ type: COURSE + "_" + GET + "_" + FAILURE, payload: error});

export const getCourse = (id) => dispatch => {
    dispatch(boundItemRequest())
    return mainAxios.get(`courses/${id}/`)
        .then(res => dispatch(boundItemSuccess(res.data)))
        .catch(err => dispatch(boundItemFailure(err.response.statusText)));
}