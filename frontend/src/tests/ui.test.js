import React from 'react';
import { CardHeader } from "../components/UI/Card";
import {shallow} from 'enzyme';


describe("Card header component", () => {
    const cardHeaderName = "Test card";
    const container = shallow(<CardHeader name={cardHeaderName}/>);

    it('should match the snapshot', () => {
        expect(container.html()).toMatchSnapshot();
    });

    it('should have a text', () => {
        expect(container.find('h4').text()).toEqual(cardHeaderName);
    });

    it('should have a line', () => {
        expect(container.exists('hr')).toEqual(true);
    });
});