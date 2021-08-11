import requests
import json
URL='http://127.0.0.1:8000/student/'



def get_method(id=None):
    data={'id':id}
    json_data=json.dumps(data)
    header={'content-type':'application/json'}
    res=requests.get(url=URL, headers=header , data=json_data)
    print(res.json())
    
def post_data():
    data={
        'name':'raja',
        'roll':102,
        'city':'pat'
    }
    json_data=json.dumps(data)
    header={'content-type':'application/json'}
    res=requests.post(url=URL, headers=header , data=json_data)
    print(res.json())



def put_data():
    data={
        "id":4,
        'name':'raja',
        'roll':102,
        'city':'pat'
    }
    json_data=json.dumps(data)
    header={'content-type':'application/json'}
    res=requests.put(url=URL, headers=header , data=json_data)
    print(res.json())



put_data()
