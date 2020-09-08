import { Calendar } from '@fullcalendar/core';
import interactionPlugin from '@fullcalendar/interaction';
import dayGridPlugin from '@fullcalendar/daygrid';
import timeGridPlugin from '@fullcalendar/timegrid';
import listPlugin from '@fullcalendar/list';
import moment from 'moment';
import { getCookie } from '../../tools/coockies';


document.addEventListener('DOMContentLoaded', function() {
  var calendarEl = document.getElementById('schedule');
  var formatTime = 'YYYY-MM-DD HH:mm:ss';

  if (calendarEl !== null) {
      var calendar = new Calendar(calendarEl, {
        plugins: [ interactionPlugin, dayGridPlugin, timeGridPlugin, listPlugin ],
        initialView: 'dayGridMonth',
        locale: 'ru',
        headerToolbar: {
          left: 'prev,next today',
          center: 'title',
          right: 'dayGridMonth,timeGridWeek,timeGridDay'
        },
        events: function(fetchInfo, successCallback, failureCallback) {
            $.ajax({
                url: '/schedule/list',
                dataType: 'json',
                method: 'POST',
                data: {
                    csrfmiddlewaretoken: getCookie('csrftoken'),
                    start: moment(fetchInfo.start).format(formatTime),
                    end: moment(fetchInfo.end).format(formatTime)
                },
                success: function(doc) {
                    var events = [];
                    doc.forEach(function (item) {
                        events.push({
                            groupId: item.groupId,
                            title: item.title,
                            url: item.url,
                            start: item.start,
                            end: item.end
                        });
                    });
                    successCallback(events);
                }
            });
        }
      });

      calendar.render();
  }
});