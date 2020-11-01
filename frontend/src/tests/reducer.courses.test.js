import { GET, REQUEST, SUCCESS, FAILURE, COURSE_LIST } from '../constants/ActionTypes';
import coursesReducer, { initialState } from '../reducers/coursesReducers';
import {initialStateCoursesWithError, dataListCourses} from "./test-data";


describe('Courses reducer', () => {

    it(COURSE_LIST + "_" + GET + "_" + REQUEST, () => {
        const action = {
            type: COURSE_LIST + "_" + GET + "_" + REQUEST,
        }
        const expectedAction = {
            ...initialState,
            loading: true
        }

        expect(coursesReducer(initialState, action)).toEqual(expectedAction)
    });

    it(COURSE_LIST + "_" + GET + "_" + REQUEST + ' after error', () => {
        const action = {
            type: COURSE_LIST + "_" + GET + "_" + REQUEST,
        }
        const expectedAction = {
            ...initialStateCoursesWithError,
            loading: true,
            error: null
        }

        expect(coursesReducer(initialStateCoursesWithError, action)).toEqual(expectedAction)
    });

    it(COURSE_LIST + "_" + GET + "_" + SUCCESS, () => {
        const action = {
            type: COURSE_LIST + "_" + GET + "_" + SUCCESS,
            payload: dataListCourses
        }
        const expectedAction = {
            ...initialState,
            loading: false,
            items: dataListCourses,
        }

        expect(coursesReducer(initialState, action)).toEqual(expectedAction)
    });

    it(COURSE_LIST + "_" + GET + "_" + FAILURE, () => {
        const action = {
            type: COURSE_LIST + "_" + GET + "_" + FAILURE,
            payload: 'Not found'
        }
        const expectedAction = {
            ...initialState,
            loading: false,
            error: 'Not found'
        }

        expect(coursesReducer(initialState, action)).toEqual(expectedAction)
    });
})