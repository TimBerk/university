import React, { Fragment } from 'react';
import {BrowserRouter as Router, Switch, Route, Redirect} from 'react-router-dom';

import { Header } from "../components/Header";
import { MainPage, CoursePage, LoginPage, SchedulePage, UserCoursesPage, ProfilePage } from './index';

const AppRouter = () => {
    return <Fragment>
        <Router>
            <Header />

            <Switch>
                <Route
                    path="/"
                    component={MainPage}
                    exact
                />

                <Route
                    path="/course/:id"
                    component={CoursePage}
                />

                <Route
                    path="/schedule/"
                    component={SchedulePage}
                    exact
                />

                <Route
                    path="/login"
                    component={LoginPage}
                />

                <Route
                    path="/my/courses"
                    component={UserCoursesPage}
                />

                <Route
                    path="/profile/"
                    component={ProfilePage}
                />
            </Switch>
        </Router>
    </Fragment>
}

export default AppRouter;