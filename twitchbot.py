import time
from twitchobserver import Observer

BOT_USERNAME = 'chad__bot'
OAUTH_TOKEN = 'oauth:' + '3kijtmb8di9auccugwhpp46ce176ta'

with Observer(BOT_USERNAME, OAUTH_TOKEN) as observer:
    observer.join_channel('chad__bot')

    while True:
        try:
            for event in observer.get_events():
                if event.type == 'TWITCHCHATMESSAGE':
                    print(event.message)

            time.sleep(1)

        except KeyboardInterrupt:
            observer.leave_channel('channel')
            break