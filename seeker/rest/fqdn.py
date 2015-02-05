import requests
from rest_framework.reverse import reverse
import re
import json

class FQDN:
    def __init__(self,request,data):
        self.request = request
        self.data = data


    def search(self):
        if 'hostname' in self.data:
            l = []
            url = reverse('lookup-list', request=self.request, format=None)
            hostname = self.data['hostname']
            r = requests.get(url)
            r = r.json()
            for i in r:
                if bool(re.match(i['pattern'],hostname)):
                    l.append(i)

            if len(l) == 0:
                return {'results' : 'no matches found for that hostname'}

            if 'alert' in self.data:
                a = []
                alert = self.data['alert']
                for j in l:
                    if alert in j['alert_set']:
                        a.append(j)


                if len(a) == 0:
                    return {'results' : 'no hostname alert match found'}


                return {'results': a}
            return {'results' : l}
        else:
            return {'error' : 'no hostname provided'}