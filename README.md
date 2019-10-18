# MAMoC-Server
This is the server component of MAMoC, Multisite Adaptive Mobile Computation Offloading Framework to offload compute-intensive tasks from mobile devices to more powerful surrogates including nearby devices, edge devices and remote cloud instances.

The server side of MAMoC contains two components: `mamoc_router` and `mamoc_server`. The router is decoupled and can be hosted separately with the server.

## Citation
If you use this server runtime environment in your work, don't forget to cite the following paper please:
```
D. Sulaiman and A. Barker, "MAMoC-Android: Multisite Adaptive Computation Offloading for Android Applications," 
2019 7th IEEE International Conference on Mobile Cloud Computing, Services, and Engineering (MobileCloud), Newark, CA, USA, 2019, pp. 68-75.
```
[Link to the paper](https://ieeexplore.ieee.org/document/8710699)

## Usage

### Docker (Server and Router)
You can pull the docker images from Docker hub and run them on your server:
```
docker pull dawan/mamoc_router
docker run -it -d --name "mamoc-router" -p 8080:8080 dawan/mamoc_router

docker pull dawan/mamoc_server
docker run --rm -it --name "mamoc-server" --network="host" dawan/mamoc_server
```

### Client
The main usage of MAMoC server is to serve the offloading requests from the mobile applications built on top of [MAMoC framework](https://github.com/dawand/MAMoC-Android).

To install the required libraries, run the following:

```python
sudo python3 setup.py install
```

Then, you can run the following python client program to test its functionality:

```python
python3 TestClient.py
```

Make sure both the server and the router components are running and listening to requests at `localhost:8080`

## Build
### Server and Router
You need to make sure that the crossbar router is running before running the server. The configuration file of the crossbar router is found under mamoc_router directory.

Enter the following in the terminal to get the router running
```python
pip3 install crossbar
cd mamoc_router
crossbar start
```

In order to run the server, type in the main directory: 
```python
sudo python3 setup.py install
python3 app.py
```

### Docker
Alternatively, clone this git and navigate to `mamoc_router` and start building the docker
``` 
cd mamoc_router
docker build -t mamoc_router .
```

Once the router image is added to your docker images, run it as the following:

```
docker run -it -d -p 8080:8080 --name "mamoc-router" mamoc_router
```

To run the server, in the main directory, build the docker

```
docker build -t mamoc_server .
```

Then run the docker

```
docker run -it -d --network="host" --name "mamoc-server" mamoc_server
```

## Application Refactoring

MAMoC Server also diassembles and decompiles Android APKs to analyse the classes and methods. The source code is examined for identifying classes which are not dependant on native device features. Have a look at [ApplicationRefactor.py](ApplicationRefactor.py) file to understand how it works.

To execute the application refactoring on an APK, add the Application name and APP ID to the apps_list.txt file, and run:

```python
python3 ApplicationRefactor.py
```
You can view the number of classes, methods, filtered classes (internal classes derived from the .dex file), and offloadable classes (classes which do not have dependencies on Android platform).

## Credits
1. [Crossbar + Autobahn](https://crossbar.io/autobahn/)
2. [OpenJDK Docker images](https://hub.docker.com/_/openjdk/)
3. [AndroGuard](https://github.com/androguard/androguard)