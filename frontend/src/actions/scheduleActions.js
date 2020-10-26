import Cookies from 'universal-cookie';
import moment from 'moment';

import { GET_SCHEDULE_LIST, GET_SCHEDULE} from "../constants/ActionTypes";
import { mainAxios, csrfAxios, checkOrSetCsrfToken } from '../utils';


const formatTime = 'YYYY-MM-DD HH:mm:ss';


export const getCalendar = (fetchInfo, successCallback) => dispatch => {
    
    const cookies = new Cookies();
    const csrfToken = cookies.get('csrftoken');
    const currentAxios = csrfAxios(csrfToken)

    const today = moment();
    let start = today.startOf('week').toString();
    let end = today.endOf('week').toString();

    if (fetchInfo) {
        start = fetchInfo.hasOwnProperty('start') ? fetchInfo.start : undefined;
        end = fetchInfo.hasOwnProperty('end') ? fetchInfo.end : undefined;
    }

    start = moment(start).format(formatTime);
    end = moment(end).format(formatTime);

    let data =  {
        start,
        end
    }
    
    currentAxios.post(`schedule/calendar/`, data)
        .then(response => {
            let events = [];
            response.data.forEach(function (item) {
                events.push({
                    groupId: item.groupId,
                    title: item.title,
                    url: item.url,
                    start: item.start,
                    end: item.end
                });
            });
            dispatch({
                type: GET_SCHEDULE_LIST,
                payload: events
            })
            successCallback(events)
        })
        .catch(errors => {
            console.log(errors);

            if (errors.response.status === 403) {
                dispatch(checkOrSetCsrfToken());
            }
        });
}

export const getSchedule = (id) => dispatch => {
    mainAxios.get(`schedule/${id}/`)
        .then(response => {
            dispatch({
                type: GET_SCHEDULE,
                payload: response.data
            })
        })
        .catch((err) => console.log(err));
}