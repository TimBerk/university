import { GET_COURSE_LIST, GET_COURSE } from '../constants/ActionTypes';

const courseReducer = (state, action) => {
    if (state === undefined) {
        return {
            items: [],
            course: null,
            loading: true,
            error: false
        }
    }

    switch (action.type) {
        case GET_COURSE_LIST:
            return {
                ...state,
                items: action.payload,
                loading: false
            };
        case GET_COURSE:
            return {
                ...state,
                course: action.payload,
                loading: false
            };
        default:
            return state
    }
}

export default courseReducer;