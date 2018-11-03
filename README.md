# MAMoC-Server
This is the server component of MAMoC, Multisite Adaptive Mobile Computation Offloading Framework 
to offload compute-intensive tasks from mobile devices to more powerful surrogates including nearby devices, edge devices and remote cloud instances.

##Setup

It is tested on Ubuntu 16.04 and MacOS 10.12

The router can be hosted separately with the server. The configuration file of the crossbar router is found under mamoc_router directory.

### Requirements
- Python >= 3.5
- Docker Engine for running docker containers

### Docker

You need to setup the router before running the server. In order to run the docker container for the router, navigate to `mamoc_router` 
and start building the docker

``` 
cd mamoc_router
docker build -t mamoc_router Dockerfile .
```

Once the router image is added to your docker images, run it as the following:

```
docker run -it -d --name "mamoc-router" mamoc_router
```

To run the server, in the main directory, build the docker

```
docker build -t mamoc_server Dockerfile .
```

Then run the docker

```
docker run -it -d --name "mamoc-server" --network="host" -p 8080:8080 mamoc_server
```

### Running locally
In the main directory, run 

```
python setup.py install
```

You need to make sure that the crossbar router is running before running the server.

Enter the following in the terminal to get the router running

```
pip install crossbar
cd mamoc_router
crossbar start
```

##Credits
[1] Crossbar

[2] Autobahn

[3] OpenJDK Docker images