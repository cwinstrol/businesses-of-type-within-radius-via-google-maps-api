import requests,json

#key=''
radius='50000'
type='book_store'
keyword=''
location='39.16285,-84.81207'

r=requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+location+'&radius='+radius+'&type='+type+'&key='+key+')

with open('c:\\users\\user\\downloads\\nearbySearch.json','w') as f:
    f.write(json.dumps(r.json(), indent=4, sort_keys=True))

ar=[]
with open('c:\\users\\user\\downloads\\nearbySearch.json') as f:
    data=json.load(f)
    for i in data['results']:
        #sort for names like dominos
        ar.append(i['place_id'])

with open('c:\\users\\user\\downloads\\details.json','w') as f:
d={}
for placeid in ar:
    r=requests.get('https://maps.googleapis.com/maps/api/place/details/json?placeid='+placeid+'&key='+key)
    data=r.json()
    k=data['result']['name']
    d[k]=data

with open('c:\\users\\user\\downloads\\details.json') as f:
    data=json.load(f)
    ar=[]
    for k,v in data['result'].items():
        ar.append(v)
    print(ar)
