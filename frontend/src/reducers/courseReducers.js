import {GET, REQUEST, SUCCESS, FAILURE, COURSE} from '../constants/ActionTypes';

const initialState = {
    course: null,
    loading: false,
    error: null
}

const courseReducer = (state = initialState, action) => {

    switch (action.type) {
        case COURSE + "_" + GET + "_" + REQUEST:
          return {
            ...state,
            loading: true,
            error: null,
          }
        case COURSE + "_" + GET + "_" + SUCCESS:
          return {
            ...state,
            loading: false,
            course: action.payload,
          }
        case COURSE + "_" + GET + "_" + FAILURE:
          return {
            ...state,
            loading: false,
            error: action.payload,
          }
        default:
            return state
    }
}


export default courseReducer;