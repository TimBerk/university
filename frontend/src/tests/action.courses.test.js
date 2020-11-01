import configureStore from 'redux-mock-store';
import thunk from 'redux-thunk';
import MockAdapter from 'axios-mock-adapter';
import { mainAxios } from "../utils";

import { GET, REQUEST, SUCCESS, FAILURE, COURSE_LIST } from '../constants/ActionTypes';
import { getCourseList } from "../actions/courseAction";
import { dataListCourses } from "./test-data";


const middlewares = [thunk];
const mockStore = configureStore(middlewares);
const mock = new MockAdapter(mainAxios);
const store = mockStore({});

describe('Course list', () => {

    beforeEach(() => {
        store.clearActions();
    });

    it(COURSE_LIST + "_" + GET + "_" + SUCCESS, () => {

        mock.onGet('courses/').reply(200, {
             results: dataListCourses, status: 'ok',
        });

        store.dispatch(getCourseList())
            .then(() => {
                let expectedActions = [
                    {
                        type: COURSE_LIST + "_" + GET + "_" + REQUEST,
                    },
                    {
                        type: COURSE_LIST + "_" + GET + "_" + SUCCESS,
                        payload: dataListCourses
                    },
                ]
                expect(store.getActions()).toEqual(expectedActions);
            })
    });

    it(COURSE_LIST + "_" + GET + "_" + FAILURE, () => {

        mock.onGet('/courses-new').reply(404, {
            response: { statusText: 'Not found' }
        });

        store.dispatch(getCourseList())
            .catch(error => {
                let expectedActions = [
                    {
                        type: COURSE_LIST + "_" + GET + "_" + FAILURE,
                        payload: 'Not found'
                    },
                ]
                expect(store.getActions()).toEqual(expectedActions);
            });
    });
})