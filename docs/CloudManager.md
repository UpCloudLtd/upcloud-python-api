# Cloud Manager

CloudManager handles all HTTP communications with UpCloud and mixes in the behavior of all Manager
classes.

In addition to the credentials, CloudManager can be given a timeout parameter that is
relayed to requests library, see [here](http://docs.python-requests.org/en/master/user/advanced/?highlight=timeout#timeouts).
Default timeout is 10.

```python

# create manager and form a token
manager = CloudManager("api-username", "password")

```

# Account / Authentication

```python

manager.authenticate() # alias: get_account()
manager.get_account()

```

# Zone

Zones can be queried from the api.

```python

manager.get_zones()

```

# TimeZone

Timezone can be given as a parameter to a server during creation and update.

```python

manager.get_timezones()

```

# Pricing

```python

manager.get_prices()

```

# Server Sizes

List the possible server CPU-ram configurations.

```python

manager.get_server_sizes()

```
