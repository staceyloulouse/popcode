# Import Pushy API class
from pushy import PushyAPI

# Payload data you want to send to devices
data = {'message': 'Hello World!'}

# The recipient device tokens
to = ['cdd92f4ce847efa5c7f']

# Optionally, send to a publish/subscribe topic instead
# to = '/topics/news'

# Optional push notification options (such as iOS notification fields)
options = { 
    'notification': {
        'badge': 1,
        'sound': 'ping.aiff',
        'body': u'Hello World \u270c'
    }
}

# Send the push notification with Pushy
PushyAPI.sendPushNotification(data, to, options)