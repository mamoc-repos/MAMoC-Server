# MAMoC-Server
This is the server component of MAMoC: Multisite Adaptive Mobile Computation Offloading framework.

##Setup

It is tested on Ubuntu 16.04 and MacOS 10.12

### Bare metal

#### Requirements
- Python >= 3.5

run ``python setup.py install``

### Docker

In the main directory, build the docker

``docker build -t mamoc_server Dockerfile .``

Then run the docker

``docker run -it -d --name "mamoc-server" --network="host" -p 8080:8080 mamoc_server``

