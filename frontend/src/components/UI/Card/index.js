import React, { Fragment, Component } from 'react';

const CardHeader = (props) => {
    return (
        <Fragment>
            <h4 className="card-title">{props.name}</h4>
            <hr className="hr-light" />
        </Fragment>
    );
}

const CardBody = (props) => {
    return (
        <div className="card-body elegant-color white-text rounded-bottom">
            { props.children }
        </div>
    );
}

const CardImage = (props) => {
    const { link, alt=null } = props;
    let imageLink = (link === null) ? 'https://picsum.photos/900/200' : link;
    
    return (
        <div className="view overlay">
            <img className="card-img-top" src={imageLink} alt={alt} style={{maxHeight: 200}}/>
            <div className="mask rgba-white-slight"></div>
        </div>
    );
}

const CardText = (props) => {
    return <p className="card-text white-text mb-4">{props.text}</p>;
}

const CardLink = (props) => {
    const { name, link } = props;
    return (
        <a href={link} className="white-text d-flex justify-content-end">
            <h5>{name} <i className="fas fa-angle-double-right"></i></h5>
        </a>
    );
}

class Card extends Component {
    render() {
        const { children } = this.props;

        return(
            <div className="container">
                <div className="card">
                    { children }
                </div>
            </div>
        );
    }
}

export {
    Card,
    CardHeader,
    CardBody,
    CardImage,
    CardText,
    CardLink
}