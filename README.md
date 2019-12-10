<img src="https://user-images.githubusercontent.com/275147/59666096-283fec80-91ef-11e9-9172-ed4d2607bd08.png" width="300" height="300">

# minipinga

mini clone for pinga https://twitter.com/pinga_comic

## Getting Started

### Install Python 3.7.1

```shell
brew install pyenv
```

```shell
brew install zlib
brew install sqlite
export LDFLAGS="${LDFLAGS} -L/usr/local/opt/zlib/lib"
export CPPFLAGS="${CPPFLAGS} -I/usr/local/opt/zlib/include"
export LDFLAGS="${LDFLAGS} -L/usr/local/opt/sqlite/lib"
export CPPFLAGS="${CPPFLAGS} -I/usr/local/opt/sqlite/include"
export PKG_CONFIG_PATH="${PKG_CONFIG_PATH} /usr/local/opt/zlib/lib/pkgconfig"
export PKG_CONFIG_PATH="${PKG_CONFIG_PATH} /usr/local/opt/sqlite/lib/pkgconfig"
```

ref. <https://github.com/jiansoung/issues-list/issues/13#issuecomment-470275744>

```shell
pyenv install 3.7.1
```

```shell
brew install pipenv
PIPENV_VENV_IN_PROJECT=true pipenv --python=$(pyenv root)/versions/3.7.1/bin/python install
pipenv install --dev
```

### Tips

sometime brake pipenv.

```shell
$ pipenv -v
Traceback (most recent call last):
  File "/usr/local/Cellar/pipenv/2018.11.26_2/libexec/bin/pipenv", line 6, in <module>
    from pkg_resources import load_entry_point
(snip)
resolve
    raise DistributionNotFound(req, requirers)
pkg_resources.DistributionNotFound: The 'pipenv==2018.11.26' distribution was not found and is required by the application
```

Reinstall is easy to fix.

```shell
brew reinstall pipenv
$ pipenv -v
Usage: pipenv [OPTIONS] COMMAND [ARGS]...
```


## Prerequisites

### Cloud Firestore

```shell
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

```shell
$ gcloud functions deploy minipinga \
--memory 128 --runtime python37 \
--trigger-resource foo_bar --trigger-event google.pubsub.topic.publish \
--update-env-vars SLACK_API_TOKEN='xxxxx',SLACK_NOTIFIED_CHANNEL='xxx'
```
