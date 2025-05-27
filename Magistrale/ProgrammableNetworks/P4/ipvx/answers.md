# Questions

1. Supported switch headers are Ethernet (at LVL2) and IPv4 (at LVL3)
2. Start
   |
   parse_ethernet
   |
   | # Is ethertype 0x800?
   ^
   no /   \ yes
   accept  parse_ipv4
   |
   accept
3.  | dst_Addr       | nh_mac    | ouPort |
   | ---------------- | ----------- | -------- |
   | 192.168.1.0/24 | 00:...:00 | 1      |
   |                |           |        |
4. There are two types of metadata:
     - The standard metadata, which in this case is used for the egress_spec
     - no custom ones
5. We have the ipv4_forward, and drop_packet()