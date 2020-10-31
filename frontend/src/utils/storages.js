import Cookies from "universal-cookie";
import { parseJSON } from "jquery";

export const cookies = new Cookies();
export const getCsrfToken = () => cookies.get('csrftoken');

export const getToken = () => localStorage.getItem('token');
export const getRefreshToken = () => localStorage.getItem('refresh_token');

export const getCurrentUser = () => {
    return sessionStorage.getItem('userData') ? parseJSON(sessionStorage.getItem('userData')) : {}
}
