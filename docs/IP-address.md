

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

CloudManager returns IP-address objects.

```python

manager.get_IPs()
manager.get_IP("185.20.31.125")

```

## Create

The new IP-address must be attached to a server and has a random address.

```python

# params: server uuid or a Server object and family, for which default is IPv4
manager.attach_IP(server_uuid)
manager.attach_IP(server_uuid, "IPv4")
manager.attach_IP(server_uuid, "IPv6")
manager.attach_IP(Server)
manager.attach_IP(Server, "IPv4")
manager.attach_IP(Server, "IPv6")


# or use Server instance
server = manager.get_server(uuid)
server.add_IP() # default is IPv4
server.add_IP("IPv4")
server.add_IP("IPv6")

```

## Update

At the moment only the ptr_record (reverse DNS) of an IP can be changed.

```python

ip = manager.get_IP("185.20.31.125")
ip.ptr_record = "the.new.ptr.record"
ip.save()

```

## Destroy

```python

ip = manager.get_IP("185.20.31.125")
ip.destroy()

```
