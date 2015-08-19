from pyramid.view import view_config
from sqlalchemy import func

import datetime

from model.models import (
    DBSession,
    Measure,
)


@view_config(route_name='get_imsi_list', renderer='json')
def get_imsi_list(request):
    import random
    count = random.randrange(1, 20)
    c = 0
    result = []

    while c < count:
        imsi = random.randrange(43534534534534, 43534534534555)
        lur = random.randrange(5, 20)
        result.append({
            'id': c,
            'imsi': imsi,
            'last_lur': lur
        })
        c += 1

    result.append({
        'id': 25,
        'imsi': 40000000000000,
        'last_lur': 3
    })

    if 'jtSorting' in request.GET:
        sorting_params = request.GET['jtSorting'].split(' ')
        sorting_field = sorting_params[0]
        reverse = sorting_params[1] == 'DESC'
        result.sort(key=lambda x: x[sorting_field], reverse=reverse)

    return {
        'Result': 'OK',
        'Records': result
    }


@view_config(route_name='get_imsi_messages', renderer='json')
def get_imsi_messages(request):
    imsi = request.matchdict['imsi']
    timestamp_begin = request.GET['timestamp_begin'] if 'timestamp_begin' in request.GET else None
    timestamp_end = request.GET['timestamp_end']

    types = ['from', 'to']

    result = {
        'imsi': imsi,
        'sms': []
    }

    import random
    import string
    import time

    if timestamp_begin:
        sms_count = random.randrange(0, 2)
    else:
        sms_count = random.randrange(1, 10)

    c = 0
    while c < sms_count:
        result['sms'].append({
            'type': random.choice(types),
            'text': time.time() * 1000000,
            'sent': random.choice([True, False])
        })
        c += 1

    result['sms'] = sorted(result['sms'], key=lambda sms: sms['text'])

    return result


@view_config(route_name='get_imsi_circles', renderer='json')
def get_imsi_circles(request):
    imsi = request.matchdict['imsi']
    timestamp_begin = request.GET['timestamp_begin'] if 'timestamp_begin' in request.GET else None
    timestamp_end = request.GET['timestamp_end']

    result = {
        'imsi': imsi,
        'circles': []
    }

    import random
    import string

    if timestamp_begin:
        circles_count = random.randrange(0, 2)
    else:
        circles_count = random.randrange(1, 10)

    c = 0
    while c < circles_count:
        result['circles'].append({
            'center': [55.69452, 37.56702],
            'radius': random.randrange(30, 300)
        })
        c += 1

    return result


@view_config(route_name='send_imsi_message', request_method='POST', renderer='json')
def send_imsi_message(request):
    imsi = request.matchdict['imsi']
    text = request.body

    import random
    statuses = ['sent', 'failed']
    sent = random.choice(statuses)

    result = {
        'status': sent
    }

    return result


@view_config(route_name='start_tracking', request_method='GET', renderer='json')
def start_tracking(request):
    import time
    time.sleep(8)
    return True


@view_config(route_name='stop_tracking', request_method='GET', renderer='json')
def stop_tracking(request):
    import time
    time.sleep(8)
    return True
