import React, { Component } from 'react';

import FullCalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'
import interactionPlugin from '@fullcalendar/interaction'
import ruLocale from '@fullcalendar/core/locales/ru';

import { checkOrSetCsrfToken } from '../../utils'

export default class ScheduleCalendar extends Component {

  componentDidMount() {
    checkOrSetCsrfToken();
  }

  render() {
    const { eventsSet, eventContent} = this.props;

    return (
      <div className='mt-3'>
          <FullCalendar
            locale={ruLocale}
            plugins={[dayGridPlugin, timeGridPlugin, interactionPlugin]}
            headerToolbar={{
              left: 'prev,next today',
              center: 'title',
              right: 'dayGridMonth,timeGridWeek,timeGridDay'
            }}
            initialView='dayGridMonth'
            selectable={true}
            selectMirror={true}
            dayMaxEvents={true}
            weekends={true}
            initialEvents={ eventsSet }
            eventClick={ eventContent }
          />
      </div>
    )
  }
}