# minipinga
mini clone for pinga https://twitter.com/pinga_comic

## Prerequisites
### Cloud Firestore
```
manga_sites
  domain
  indication_text_xpath

subscriptions
  url
  title
  indication_text_value
  last_checked_date
```

### Env vars
* SLACK_API_TOKEN
* SLACK_NOTIFIED_CHANNEL

## Deploy
```
$ gcloud functions deploy minipinga \
--memory 128 --runtime python37 \
--trigger-resource foo_bar --trigger-event google.pubsub.topic.publish \
--update-env-vars SLACK_API_TOKEN='xxxxx',SLACK_NOTIFIED_CHANNEL='xxx'
```
