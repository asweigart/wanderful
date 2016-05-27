import pprint
from eventbrite import Eventbrite
import os 
import json
from datetime import datetime 

auth_key=os.environ['EVENTBRITE_KEY']

def get_event_results(q, datestring):

    datestring = datetime.strptime(datestring, "%m/%d/%Y")
    datestring = datetime.strftime(datestring, "%Y-%m-%d")
    client = Eventbrite(auth_key)
    
    # date = datetime.strptime(datestring, "%Y-%m-%d")
    # params = {"q": q, "start_date.range_start": datestring}
    start_date = datestring+"T00:00:00"
    end_date = datestring+"T23:59:59"
    popular = True
    sort_by = "best"
    
    params = {"q": q, "start_date.range_start": start_date, 
              "start_date.range_end": end_date, "sort_by": sort_by}
    print "AAAAAAAAAA", params
    search_response = client.event_search(**params)
    print search_response
    events = search_response.get('events', [])
    print events
    rendered_responses = []
    
    for event in events:
        if event.get('logo'):
            image_url = event['logo']['url']
        else:
            image_url = None
        rendered_responses.append({'name': event['name']['html'],
                                    'start': datetime.strptime(event['start']['local'], ('%Y-%m-%dT%H:%M:%S')),
                                    'status': event['status'],
                                    'url': event['url'], 
                                    'locale': event['locale'],
                                    'id': event['id'],
                                    'image':image_url})


    pprint.pprint(rendered_responses)
    return rendered_responses

