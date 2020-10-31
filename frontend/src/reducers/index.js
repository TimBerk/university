import { combineReducers } from "redux";
import course from './courseReducers';
import courses from './coursesReducers';
import lessons from './lessonReducers';
import auth from './authReducers';
import schedule from './scheduleReducers';
import user from './userReducers';

export default combineReducers({
    course,
    courses,
    lessons,
    auth,
    schedule,
    user
});