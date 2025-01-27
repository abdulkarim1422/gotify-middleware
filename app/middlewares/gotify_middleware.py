

def extract_token_from_request(request):
    try:
        token = dict(request.headers).get('x-gotify-key')
    except:
        token = ""
    if not token:
        try:
            token = dict(request.cookies).get('token')
        except:
            token = ""
    return token