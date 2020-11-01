import { GET, REQUEST, SUCCESS, FAILURE, COURSE_LIST } from '../constants/ActionTypes';

export const initialState = {
    items: null,
    loading: false,
    error: null
}

const coursesReducer = (state = initialState, action) => {
    switch (action.type) {
        case COURSE_LIST + "_" + GET + "_" + REQUEST:
          return {
            ...state,
            loading: true,
            error: null
          }
        case COURSE_LIST + "_" + GET + "_" + SUCCESS:
          return {
            ...state,
            loading: false,
            items: action.payload,
          }
        case COURSE_LIST + "_" + GET + "_" + FAILURE:
          return {
            ...state,
            loading: false,
            error: action.payload,
          }
        default:
            return state
    }
}

export default coursesReducer;