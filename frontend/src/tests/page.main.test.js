import React from 'react';
import { Provider } from "react-redux";
import { mount } from 'enzyme';

import thunk from "redux-thunk";
import configureStore from 'redux-mock-store';

import { dataListCourses } from "./test-data";
import MainPage from '../pages/MainPage';

const middlewares = [thunk];
const mockStore = configureStore(middlewares);

describe('Main Page', () => {
    let localStore;
    let component;

    beforeEach(() => {
        localStore = mockStore({
            courses: dataListCourses,
            loading: false,
            error: null
        });
        component = mount(
            <Provider store={localStore}>
                <MainPage/>
            </Provider>
        );
    });

    afterEach(() => {
        component.unmount();
    });

    it('Render page', () => {
        expect(component.html()).toMatchSnapshot();
    });

    it('Initial state', async () => {
        expect(component.find(MainPage)).toBeTruthy();
        expect(component.find('MainPage').state('items')).toEqual([]);
        expect(component.find('MainPage').state('loading')).toEqual(false);
        expect(component.find('MainPage').state('error')).toEqual(null);
    });
});