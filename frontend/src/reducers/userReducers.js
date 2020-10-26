import { GET_USER_COURSE, JOIN_TO_COURSE } from '../constants/ActionTypes';


const userCoursesReducer = (state, action) => {
    if (state === undefined) {
        return {
            courses: []
        }
    }

    switch (action.type) {
        case GET_USER_COURSE:
            return {
                ...state,
                courses: action.payload
            };
        case JOIN_TO_COURSE:
            return {
                ...state
            };
        default:
            return state
    }
}

export default userCoursesReducer;