## Create an Event
<img width="1001" alt="Screenshot 2024-02-07 at 4 05 44 PM" src="https://github.com/uzaxirr/gcal/assets/72073401/b76aafae-441f-4239-8dc5-50a8707833e0">

### cURL
````
curl --location 'http://127.0.0.1:8000/events/' \
--header 'Content-Type: application/json' \
--data '{
    "title": "Meeting",
    "createdBy": 1,
    "invites": [2],
    "startTime": "2024-02-07T10:00:00Z",
    "endTime": "2024-02-07T11:00:00Z",
    "remindBefore": 15
}
'
````
## List All the events of a Given User
<img width="1041" alt="Screenshot 2024-02-07 at 4 07 38 PM" src="https://github.com/uzaxirr/gcal/assets/72073401/9bae9842-d420-4ef8-a93f-5822e72aa044">

### cURL
````
curl --location 'http://127.0.0.1:8000/events/user/1/'
````

## Get details of a Given event
<img width="1020" alt="Screenshot 2024-02-07 at 4 08 34 PM" src="https://github.com/uzaxirr/gcal/assets/72073401/8c11ace6-fa85-4c43-be83-15e782edc268">

### cURL
````
curl --location 'http://127.0.0.1:8000/events/1/'
````
