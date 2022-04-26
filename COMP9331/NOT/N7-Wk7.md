# IP

## Header

+ IP header is 20 bytes (TCP is also 20 bytes)
+ Offset is multiple of eight

## Address

+ 4 8-bits values = 32 bits
+ Two parts
  + Subnet: High order
  + Host: Low order
    + All 1 host is a broadcast address (xxx.xxx.xxx.255)
      + No one should reject
    + All 0: Network address (xxx.xxx.xxx.0)
      + Represents the whole network

### DHCP

+ Dynamic Host Configuration Protocol

### Private IP

+ 10.0.0.0/8
+ 172.16.0.0/12
+ 192.168.0.0/16
+ Typically for NAT

## Subnet

+ Interfaces that can communicate without any router
+ Isolated network

### Mask

+ /number: 
  + How many bits are subnet part


