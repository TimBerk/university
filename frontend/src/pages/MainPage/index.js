import React, { Component } from 'react';
import { connect } from 'react-redux';
import { getCourseList } from '../../actions/courseAction';
import { CourseList } from '../../components/Course';
import {Card, CardBody, CardHeader, Spinner} from "../../components/UI";

class MainPage extends Component {
    state = {
        items: [],
        loading: false,
        error: null
    }
    componentDidMount() {
        this.props.getCourseList();
    }

    UNSAFE_componentWillReceiveProps(props) {
        if (props.loading !== this.props.loading) {
            this.setState({ loading: props.loading})
        }

        if (props.error !== this.props.error) {
            this.setState({ error: props.error})
        }

        if (props.items !== this.props.items) {
            this.setState({
                items: props.items
            })
        }
    }

    render() {
        const { items, loading, error } = this.state;

        if (loading) {
            return <Spinner />
        }

        if (error) {
            return <Card>
                <CardBody>
                    <CardHeader name='Ошибка' />
                    { error }
                </CardBody>
            </Card>
        }

        return (
            <div className='container'>
                <CourseList items={items} />
            </div>
        );
    }
}


const mapStateToProps = ({ courses: { items, loading, error } }) => {
    return { items, loading, error }
}

const mapDispatchToProps = {
    getCourseList
}

export default connect(mapStateToProps, mapDispatchToProps)(MainPage)