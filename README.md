# Robo Helper

Robo Helper will be a service application that will run robot framework tasks for you triggered based on events.

Events can be triggered by:
- Scheduled with the Robo Helper scheduler
- api call to the Robo Helper rest api
- Manually through the Robo Helper web UI

When an event is triggered all robot framework tasks that have a tag matching the event name will be executed
