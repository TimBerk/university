import { combineReducers } from "redux";
import courses from './courseReducers';
import lessons from './lessonReducers';
import auth from './authReducers';
import schedule from './scheduleReducers';
import user from './userReducers';

export default combineReducers({
    courses,
    lessons,
    auth,
    schedule,
    user
});