

## About


```
Attributes:
	access 		-- "public" or "private"
	address 	-- the IP address (string)
    family      -- "IPv4" or "IPv6"
	ptr_record 	-- the reverse DNS name (string)
	server 		-- the UUID of the server this IP is attached to (string)
```

The only updateable attribute is the `ptr_record`.
`ptr_record` and `server` are not present if /server/uuid endpoint was used.

## List / Get

CloudManager returns IPAddress objects.

```python

manager.get_ips()
manager.get_ip("185.20.31.125")

```

## Create

A new IPAddress must be attached to a server and has a random address.

```python

# params: server uuid or a Server object and family, for which default is IPv4
manager.attach_ip(server_uuid)
manager.attach_ip(server_uuid, "IPv4")
manager.attach_ip(server_uuid, "IPv6")
manager.attach_ip(Server)
manager.attach_ip(Server, "IPv4")
manager.attach_ip(Server, "IPv6")


# or use Server instance
server = manager.get_server(uuid)
server.add_ip() # default is IPv4
server.add_ip("IPv4")
server.add_ip("IPv6")

```

## Update

At the moment only the ptr_record (reverse DNS) of an IP address can be changed.

```python

ip = manager.get_ip("185.20.31.125")
ip.ptr_record = "the.new.ptr.record"
ip.save()

```

## Destroy

```python

ip = manager.get_ip("185.20.31.125")
ip.destroy()

```
