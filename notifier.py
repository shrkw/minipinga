import os
import slack


def notify(text: str):
    client = slack.WebClient(token=os.environ["SLACK_API_TOKEN"])
    response = client.chat_postMessage(
        channel=os.environ["SLACK_NOTIFIED_CHANNEL"], text=text
    )
    print(response)

