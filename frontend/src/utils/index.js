import { isEmpty } from './common';
import { getRandomBtnColor } from './colors';
import { mainAxios, csrfAxios, bearerHeader, refreshHeader, checkOrSetCsrfToken } from './requests';
import { cookies, getToken, getRefreshToken, getCurrentUser } from './storages';

export {
    isEmpty,
    getRandomBtnColor,
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