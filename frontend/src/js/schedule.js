function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


document.addEventListener('DOMContentLoaded', function() {
  var calendarEl = document.getElementById('schedule');
  var formatTime = 'YYYY-MM-DD HH:mm:ss';

  var calendar = new FullCalendar.Calendar(calendarEl, {
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
});