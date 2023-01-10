from request_and_response import Response, Request
from random import random


def controller(request: Request, timeout=int(random() * 11)):
    try:
        request.url
        return 'Done'
    except:
        return 'ne Done'
