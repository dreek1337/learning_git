


def controller(request: Request, timeout=int(random() * 11)):
    re = request
    try:
        request.url
        return 'Done'
    except:
        return 'ne Done'

print(controller(r))