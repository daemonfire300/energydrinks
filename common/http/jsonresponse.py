from django.utils import simplejson
from django.http import HttpResponse


class JsonResponse(HttpResponse):
    def __init__(self, data):
        self.set_content(data)
        x_content = self.get_content()
        super(JsonResponse, self).__init__(content=x_content,
                                           mimetype='application/json')
    def set_content(self, content):
        self.x_data = content
    def get_content(self, json_encoded=True):
        if json_encoded:
            return simplejson.dumps(self.x_data)
        else:
            return self.x_data

class Success(JsonResponse):
    def __init__(self, data):
        x = data
        content = { 'type': 'success', 'data': x}
        super(Success, self).__init__(content)


class Failure(JsonResponse):
    def __init__(self, data):
        x = data
        content = { 'type': 'error', 'data': x}
        super(Failure, self).__init__(content)

class AuthFailure(Failure):
    def __init__(self, message, code=1):
        data = { 'message': message, 'code': code }
        super(AuthFailure, self).__init__(data)
        
class AuthSuccess(Success):
    def __init__(self, session_key):
        data = { 'session_key': session_key }
        super(AuthSuccess, self).__init__(data)
