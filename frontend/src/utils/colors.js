import { getRandomInt } from "./common";

export const nameOfBtnColors = [
    'btn-elegant',
    'btn-unique',
    'btn-pink',
    'btn-purple',
    'btn-deep-purple',
    'btn-indigo',
    'btn-light-blue',
    'btn-cyan',
    'btn-dark-green',
    'btn-light-green',
    'btn-yellow',
    'btn-amber',
    'btn-deep-orange',
    'btn-brown',
    'btn-blue-grey'
];

export const getRandomBtnColor = () => {
    const randomNumber = getRandomInt(nameOfBtnColors.length);
    return nameOfBtnColors[randomNumber];
}