from random import random
from request_and_response import Response, Request


def controller(request: Request, timeout=int(random() * 11)):
    r = request(url='http://url.com', method='GET', params={'c': 2, 'm': 1}, timeout=4, status=200)
    try:
        r.url
        return 'Done'
    except:
        return 'ne Done'
print(controller(Request))