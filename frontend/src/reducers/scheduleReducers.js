import { GET_SCHEDULE_LIST } from '../constants/ActionTypes';

const scheduleReducer = (state, action) => {
    if (state === undefined) {
        return {
            items: []
        }
    }

    switch (action.type) {
        case GET_SCHEDULE_LIST:
            return {
                items: action.payload
            };
        default:
            return state
    }
}

export default scheduleReducer;