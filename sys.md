# System Design

## Design Requirements

1. Move Data
2. Store Data
3. Transform Data

**Availability**: 99, 99.9, 99.99, 99.999
- SLA. Service Level Agreenment
    - SLO. Service Level Objective

**Reliability**, **Fault Tolerance**, **Redundancy**

**Throughput**: Requests / second
**Latency**: Period of time an operation takes to complete


## Networking

Client ---> Server

**TCP**.
- Two way connection between server and client
    - 3 way handshake: SYN -> SYN/ACK -> ACK
- Packet order
- Reliable: Retransmission of lost packets
- Protocols on top of TCP: HTTP, SMTP, WebSockets

**UDP** User Datagram Protocol
- No connection between server and client is stablished
- Packets out of order
- Packets lost
- Faster than TCP
- Usages: Streaming data in realtime (WebRTC), online gaming, DNS

**DNS** Domain Name System
- Translates domain names into IP addresses

## Application Layer Protocols

**HTTP**
- Request / Response protocol
- Methods:
    - GET, POST, PUT, DELETE
- Status Codes:
    - Information 100-199
    - Successful 200-299
    - Redirection 300-399
    - Client error 400-499
    - Server error 500-599
- *SSL* Secure Socket Layer / *TLS* Transport Layer Security
    - Encrypt payload

**WebSockets**
- Handshake to stablish a connection
- Connection stays open

**API**
- REST: Loose restrictions applied to HTTP
    - Pagination, multiple data, servers are stateless
        - GET http://youtube.com/videos?limit=10&offset=0
        - GET http://youtube.com/videos?limit=10&offset=10
- GraphQL
    - Uses POST method becuase it need to seend a body with a query or mutation
- gRPC
    - Uses binary data for comunication
    - Streaming (HTTP 2)

## Caching
- Faster than other memory
- Low storage
- Strategies
    - Write-around. Write to disk
    - Write-through. Write both
    - Write-back. Write to cache only, periodically copy it to disk
- Eviction policies
    - FIFO (First In First Out). Queue
    - LRU (Least Recently Used). Queue, every read, push to top
    - LFU (Least Frequetly Used). Queue, min heap by fequency

**CDN** Content Delivery Network
- Caches static data, closer to geo location
- Push: Main server pushed data to CDNs
- Pull: Each CDN acts as a proxy to request data

## Proxies & Load Balancers
- **Forward**: Client --> Proxy --> Server
- **Reverse**: Client --> Proxy <-- Server
    - CDN
    - Load Balancer

**Load Balancer**
- Layer 4 (TCP): Faster but limited
- Layer 7 (App): Slower but has more context
- Strategies
    - Round Robin
    - Weighted Round Robin
    - Location
    - Hashing

**Consistent Hashing**
- Hash key
- Hash function
- Nodes
- Place nodes in a circle, map requests to the closest clock wise

## Storage
### SQL
**RDBMS** (Relational Database Management Systems)
- Stored on disk (B + Tree)
- Have schema
- Stores Tables
    - Columns are fields
    - Rows are entries
- Have constraints
- Properties
    - **A** Atomocity
        - Every transaction is all or nothing
    - **C** Consistency
        - Data consistency
        - Follows constraints
    - **I** Isolation
        - Transactions are serialized
        - Multiple transactions happen in order 
    - **D** Durability
        - Data is persisted (stored in disk)

### NoSQL
Non-relational DBs

**Scale up better than SQL**
- No constraints
- Properties
    - **Ba**
    - **S**
    - **E** Eventual Consistency
        - Data in sycn between replicas
        - One leader (R/W) _node_, multiple _followers_ (R)

Variations:
- Key-Value
    - Simple
    - Fast
    - Ex: Redis, Memcached, etcd
- Document Store
    - Collections of documents (JSON-like nested key-value pairs)
    - Flexible, no schema
    - Ex: MongoDB
- Wide-Column
    - Big Scale
    - Write oriented
    - Ex: Cassandra, BigTable
- Graph DB
    - Relations
    - Directed Graphs

### Replication
Replicate one node into multiple ones
Types:
- Leader / Follower: Leader replicates data to _followers_
    - Leader (Read/Write)
    - Followers (Read)
- Leader / Leader: Data is replicated to multiple leaders

### Sharding
Partition data into multiple nodes

Strategies
- Range based
- Hash based

### CAP Theorem
Distribuited data

**C** Consistency. Every read will get the most up-to date data
**A** Availability. Every node will respond to requests
**P** Partition Tolerance. System will continue to function when there's a network partition 

Given P, choose A or C. Else, favor Latency or Consistency


### Object Storage
Similar to a Flat File System

Ex: S3

BLOB (Binary Large Object) Storage
Ex: Images, video


## Message Queues
Large amount of application events going fast
Process events async
Events are durable

Processing types
- Pull
- Push
- Ack

**Pub/Sub**
- Many to many
- Publisher: Event producer
- Subscriber: Event consumer
- Event ---> Topic --> Sub
                   |-> Sub

## MapReduce
Process large amounts of data

Types of processing
- Batch
    - Data up front
- Streaming
    - Real time data
