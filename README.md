# Landbot Backend Challenge

## Description

The product department wants a system to be notified when a customer requests assistance from a bot. The bot will make an http call (like a webhook) with the following information:

- Topic: a string with values can be sales or pricing
- Description: a string with a description of the problem that needs assistance from.

You need to expose an API endpoint that will receive this call and depending on the selected topic will forward it to a different channel:

``` 
Topic    | Channel   
----------------------
Sales    | Slack
Pricing  | Email
```

## Notes:
- Slack and Email are suggestions. Select one channel that you like the most, the other can be a mock.
- There may be more topics and channels in the future.

## The solution should:
- Be written in your favorite language and with the tools with which you feel comfortable.
- Be coded as you do daily (libraries, style, testing...).
- Be easy to grow with new functionality.
- Be a dockerized app.

## Development approach:
- Three Django apps were create so the models Channels, Topics and Notifications can evolve independently.
- Channels model will hold all channels, Topics will hold all topics and Notifications will hold notifications which are unique topics with a channel associated.
- There may be more services and they'll all notify so an interface was added so any new notification service added conforms to the interface.
- Since the /api/notification/ endpoint is synchronous and the notification is sent as part of the handling of the view, a task queue was added and the actual notification (it was done for the email notification) is deferred with a task.

## Run application:

- To build the image and run the services:
```
make recreate
```

- To run the task worker:
```
make task-queue
```

## Tests

```
make test
```

## API Usage:

- Load data fixtures

```
make loaddata
```

- Send request

```
curl --url http://localhost:8001/api/notification/ --header 'content-type: application/json' --data '{"topic":"Sales","description":"A description"}'
```
