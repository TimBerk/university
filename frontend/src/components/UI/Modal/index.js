import React, { Component } from 'react';

class Modal extends Component {
    render() {
        const { id, header, show, onClose, children} = this.props;

        let classModal = 'modal fade right';
        let displayModal = show ? 'block': 'none';

        if (show) {
            classModal += ' show';
        }

        return (
            <div className={classModal} id={id} tabIndex="-1" role="dialog" style={{display: displayModal}}  aria-hidden="true">
                <div className="modal-dialog modal-full-height modal-right modal-dialog-scrollable" role="document">
                    <div className="modal-content">
                        <div className="modal-header">
                            <h4 className="modal-title w-100" id="myModalLabel">{header}</h4>
                            <button type="button" className="close" data-dismiss="modal" aria-label="Close" onClick={onClose}>
                                <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                        <div className="modal-body">
                            { children }
                        </div>
                        <div className="modal-footer justify-content-center">
                            <button type="button" className="btn btn-danger" data-dismiss="modal" onClick={onClose}>Закрыть</button>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default Modal;