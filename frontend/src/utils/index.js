import { isEmpty } from './common';
import { getRandomBtnColor } from './colors';
import { BASE_URL, mainAxios, csrfAxios, bearerHeader, refreshHeader, checkOrSetCsrfToken } from './requests';
import { cookies, getToken, getRefreshToken, getCurrentUser } from './storages';

export {
    isEmpty,
    getRandomBtnColor,
    BASE_URL,
    mainAxios,
    csrfAxios,
    bearerHeader,
    refreshHeader,
    checkOrSetCsrfToken,
    cookies,
    getToken,
    getRefreshToken,
    getCurrentUser
};