# 01 - Virtualization

## 1 - Virtual Machine

VM Details:

Base Memory: 4096 MB
Storage Capacity: 40,00 GB

In Terminal:

`free -mh`:
**free** value for "Mem": 2.6Gi
`df /dev/sda1 -h`:
**Avail** value for "sda1": 28G

## 2 - Container

```bash
[dmitriy@eos-virtualbox ~]$ free -mh
               total        used        free      shared  buff/cache   available
Mem:           3.8Gi       771Mi       2.5Gi       7.1Mi       786Mi       3.1Gi
Swap:          4.0Gi          0B       4.0Gi
[dmitriy@eos-virtualbox ~]$ df /dev/sda1 -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        36G  6.3G   28G  19% /
[dmitriy@eos-virtualbox ~]$ docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

[...]

[dmitriy@eos-virtualbox ~]$ free -mh
               total        used        free      shared  buff/cache   available
Mem:           3.8Gi       746Mi       2.5Gi       7.1Mi       786Mi       3.1Gi
Swap:          4.0Gi          0B       4.0Gi
[dmitriy@eos-virtualbox ~]$ df /dev/sda1 -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        36G  6.3G   28G  19% /
```

## 3 - Draw the virtualization stack

*Made it in ASCII*

```
+-----------------------------------------+
|         Application: hello-world        |  (7)
+-----------------------------------------+
|             Container: CELL             |  (6)
+-----------------------------------------+
|   Operating System: EndeavourOS Linux   |  (5)
+-----------------------------------------+
|              Virtual Machine            |  (4)
+-----------------------------------------+
|                Hypervisor               |  (3)
+-----------------------------------------+
|       Operating System: Windows 10      |  (2)
+-----------------------------------------+
|           Bare Metal: Laptop            |  (1)
+-----------------------------------------+
```