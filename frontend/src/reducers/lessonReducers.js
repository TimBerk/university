import { GET_LESSON_LIST, GET_LESSON } from '../constants/ActionTypes';

const courseReducer = (state, action) => {
    if (state === undefined) {
        return {
            items: [],
            lesson: null,
            loading: true,
            error: false
        }
    }

    switch (action.type) {
        case GET_LESSON_LIST:
            return {
                ...state,
                items: action.payload,
                loading: false
            };
        case GET_LESSON:
            return {
                ...state,
                lesson: action.payload,
                loading: false
            };
        default:
            return state
    }
}

export default courseReducer;