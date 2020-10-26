import { LOGIN_REQUEST, LOGOUT_REQUEST, GET_USER_DATA, REFRESH_TOKEN, GET_CSRF_TOKEN } from "../constants/ActionTypes";


export default function (state, action) {

    if (state === undefined) {
        return  {
            token: null,
            refresh_token: null,
            user: {},
            isLoggedIn: false
        }
    }
    switch (action.type) {
        case LOGIN_REQUEST:
            return {
                ...state,
                token: action.payload,
                refresh_token: action.refresh_token,
                isLoggedIn: true
            };
        case GET_USER_DATA:
            return {
                ...state,
                user: action.payload
            };
        case REFRESH_TOKEN:
            return {
                ...state,
                token: action.payload
            };
        case GET_CSRF_TOKEN:
            return {
                ...state
            };
        case LOGOUT_REQUEST:
            return {
                token: null,
                refresh_token: null,
                user: {},
                isLoggedIn: false
            };
       
        default:
            return state
    }
}