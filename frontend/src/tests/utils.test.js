import { isEmpty, getRandomBtnColor, refreshHeader, bearerHeader } from "../utils";
import { nameOfBtnColors } from "../utils/colors";


describe("Is empty function", () => {
    test("Check if dictionary not empty", () => {
        const notEmptyDict = { email: "admin@uni.ru", username: 'admin', first_name: "", last_name: "Администратор" };

        expect(isEmpty(notEmptyDict)).toEqual(false);
    });

    test("Check if dictionary is empty", () => {
        const emptyDict = { };

        expect(isEmpty(emptyDict)).toEqual(true);
    });
});


describe("Random button class", () => {
    test("Check that btn class exist in array buttons", () => {
        const btnClass = [getRandomBtnColor()];

        expect(nameOfBtnColors).toEqual(
          expect.arrayContaining(btnClass),
        );
    });
});

describe("Refresh header", () => {
    test("Check empty refresh header", () => {
        const input = refreshHeader()
        const output = {}

        expect(input).toEqual(output);
    });

    test("Check refresh header with test token", () => {
        const token = 'test token'
        localStorage.setItem('refresh_token', token);

        const input = refreshHeader()
        const output = { refresh: token }

        expect(input).toEqual(output);
    });
});

describe("Bearer header", () => {
    test("Check empty bearer header", () => {
        const input = bearerHeader()
        const output = {}

        expect(input).toEqual(output);
    });

    test("Check bearer header with test token", () => {
        const token = 'test token'
        localStorage.setItem('token', token);
        const input = bearerHeader()
        const output = { headers: { Authorization: ` Bearer ${token}` } }

        expect(input).toEqual(output);
    });
});