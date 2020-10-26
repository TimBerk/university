import React, { Fragment } from 'react';
import { Link } from "react-router-dom";

const List = ({ items }) => {
    return (
        <div className="row mt-3">
            {
                items.map((course) => {
                    const link = '/course/' + course.id
                    return <div className="card col-12 mb-3" key={course.id}>
                        <div className="card-body">
                            <h4 className="card-title">{course.name}</h4>

                            <p className="card-text" dangerouslySetInnerHTML={{ __html: course.description }} />

                            <div className="btn-group">
                                <Link to={link} className="btn btn-amber btn-md">
                                    Просмотреть
                                </Link>
                            </div>
                        </div>
                    </div>
                })
            }
        </div>
    );
}

const CourseList = (props) => {
    const { items, name = 'Список курсов' } = props;

    return ( 
        <Fragment>
            <h2 className="text-center mt-5 mb-2">{name}</h2>

            <List items={ items } />
        </Fragment>
    );
}

export default CourseList;