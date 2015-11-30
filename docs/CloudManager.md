# Account / Authentication

```python

# create manager and form a token
manager = CloudManager("api-username", "password")

# test token
manager.authenticate() # alias: get_account()
manager.get_account()

```

# Zone

Zones are already hardcoded as Enums in `upcloud_api.ZONE`. However, they can be queried from the API too.

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

manager.get_pricing()

```

# Server Sizes

List the possible server CPU-ram configurations.

```python

manager.get_server_sizes

```
