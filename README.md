# MAMoC-Server
This is the server component of MAMoC, Multisite Adaptive Mobile Computation Offloading Framework 
to offload compute-intensive tasks from mobile devices to more powerful surrogates including nearby devices, edge devices and remote cloud instances.

## Setup

This setup is tested on Ubuntu 16.04 and MacOS 10.13

The server side of MAMoC contains two components: router and server. The router can be hosted separately with the server. 
The configuration file of the crossbar router is found under mamoc_router directory.

### Requirements
- Python >= 3.5
- Crossbar
- Docker Engine for running docker containers

## Docker

You can pull the docker images from Docker hub and run them on your server:

```
docker pull dawan/mamoc_router
docker run -it -d --name "mamoc-router" -p 8080:8080 dawan/mamoc_router

docker pull dawan/mamoc_server
docker run --rm -it --name "mamoc-server" --network="host" dawan/mamoc_server

```

Alternatively, clone this git and navigate to `mamoc_router` and start building the docker

``` 
cd mamoc_router
docker build -t mamoc_router Dockerfile .
```

Once the router image is added to your docker images, run it as the following:

```
docker run -it -d -p 8080:8080 --name "mamoc-router" mamoc_router
```

To run the server, in the main directory, build the docker

```
docker build -t mamoc_server Dockerfile .
```

Then run the docker

```
docker run -it -d --network="host" --name "mamoc-server" mamoc_server
```

### Running locally
In the main directory, run 

```
python setup.py install
python app.py
```

You need to make sure that the crossbar router is running before running the server.

Enter the following in the terminal to get the router running

```
pip install crossbar
cd mamoc_router
crossbar start
```


## Credits

[1] [Crossbar + Autobahn](https://crossbar.io/autobahn/)

[2] [OpenJDK Docker images](https://hub.docker.com/_/openjdk/)