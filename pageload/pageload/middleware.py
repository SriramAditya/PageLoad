import json
from datetime import date
class ExecutionFlowMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        response = self.get_response(request)
        self.f = open("pageload.json", "a")
        username = "empty"
        path_info= request.path_info
        if (path_info != '/' and request.POST.get("username")!=None):
            username = request.POST.get("username")
        self.data = {
            'path_info': path_info,
            'browser_info': request.headers['User-Agent'],
            "request_data":{},
            'method': request.method,
            "visited_by" : username,
            "ipaddress" : request.META['REMOTE_ADDR'],
            "date" : str(date.today()),
        }
        self.dump = json.dumps(self.data)
        if(path_info == '/' or path_info != '/pageload/'):
            self.f.write(self.dump)
            self.f.write("\n")
        self.f.close()
        return response
