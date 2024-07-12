

# About

Firewall is configured with FirewallRule objects that are specific to each server.
Please note that a servers firewall rules are ignored if firewall is turned off
(see [Server](/server) and [API documentation](https://developers.upcloud.com/1.3/8-servers/#modify-server)).

If a server is removed, its firewall and thus its firewall rules are removed too.

Please refer to the [API documentation](https://developers.upcloud.com/1.3/11-firewall/#create-firewall-rule)
for more info on the attributes of FirewallRule.

## List / Get

```python
server = manager.get_servers()[0]

# all firewall rules
firewall_rules = server.get_firewall_rules()
```

## Create

```python
server = manager.get_servers()[0]

rule = server.add_firewall_rule(
    FirewallRule(
        position = "1",
        direction = "in",
        family = "IPv4",
        protocol = "tcp",
        source_address_start = "192.168.1.1",
        source_address_end = "192.168.1.255",
        destination_port_start = "22",
        destination_port_end = "22",
        action = "accept"
    )
)
```

### Configure Firewall

Server provides a helper function to add several firewall rules in series.
Please note that the function does not know about pre-existing rules
(UpCloud servers are created without any firewall rules by default).

```python
server = manager.get_servers()[0]

rules = server.configure_firewall(
    [
        FirewallRule(
            position = "1",
            direction = "in",
            family = "IPv4",
            protocol = "tcp",
            source_address_start = "192.168.1.1",
            source_address_end = "192.168.1.255",
            destination_port_start = "22",
            destination_port_end = "22",
            action = "accept"
        ),
        FirewallRule(
            position = "2",
            direction = "in",
            family = "IPv4",
            protocol = "tcp",
            source_address_start = "192.168.1.1",
            source_address_end = "192.168.1.255",
            destination_port_start = "21",
            destination_port_end = "21",
            action = "accept"
        )
    ]
)
```

## Destroy

```python
server = manager.get_servers()[0]
server.get_firewall_rules()[0].destroy()
```

### Destroying all firewall rules

Due to how the API handles positions, the following will NOT work:

```python
# does NOT work
for rule in server.get_firewall_rules():
    rule.destroy()
```

This is because rules are based on position and the positions are always so
that they start from 1 and are increment by one for each consecutive rule.

A better approach would be to use CloudManager/FirewallManager directly
(CloudManager and its mixins provide API functionality to Server, Storage, FirewallRule, etc. objects)

```python
for rule in server.get_firewall_rules():
    manager.delete_firewall_rule(server.uuid, 1)
```




