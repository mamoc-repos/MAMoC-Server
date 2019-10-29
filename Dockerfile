### 1. Get Linux
FROM alpine:latest as build

# Default to UTF-8 file.encoding
ENV LANG C.UTF-8

# 2. Get openJDK
ENV JAVA_HOME /opt/openjdk-14
ENV PATH $JAVA_HOME/bin:$PATH

# https://jdk.java.net/
ENV JAVA_VERSION 14-ea+15
ENV JAVA_URL https://download.java.net/java/early_access/alpine/15/binaries/openjdk-14-ea+15_linux-x64-musl_bin.tar.gz
ENV JAVA_SHA256 76091da1b6ed29788f0cf85454d23900a4134286e5feb571247e5861f618d3cd
# "For Alpine Linux, builds are produced on a reduced schedule and may not be in sync with the other platforms."

RUN echo "Downloading OpenJDK " && \
	wget -O /openjdk.tgz "$JAVA_URL" && \
	echo "$JAVA_SHA256 */openjdk.tgz" | sha256sum -c - && \
	mkdir -p "$JAVA_HOME" && \
	tar --extract --file /openjdk.tgz --directory "$JAVA_HOME" --strip-components 1 && \
	rm /openjdk.tgz

# RUN echo "modularity of the JVM and produce a custom Java runtime for your app (using jlink). This will cut your runtime size by at least 50% in size."

# RUN ["/opt/openjdk-14/bin/jlink", "--compress=2", \
#     "--module-path", "/opt/openjdk-14/jmods/", \
#     "--add-modules", "java.base", \
#     "--output", "/jlinked"]

#FROM alpine:latest
#COPY --from=build /jlinked /opt/openjdk-14

#ENV JAVA_HOME /opt/openjdk-14
#ENV PATH $JAVA_HOME/bin:$PATH
#CMD ["$JAVA_HOME/java", "--version"]

### 3. Get Python, PIP
ENV PYTHONUNBUFFERED=1

RUN echo "**** install Python ****" && \
    apk add --no-cache python3 && \
    if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python ; fi && \
    \
    echo "**** install pip ****" && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools wheel && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi

#RUN apk add --no-cache --virtual .build-deps gcc musl-dev
#RUN pip install cython
#RUN apk del .build-deps gcc musl-dev

### 4. Set JAVA_HOME
# ENV JAVA_HOME="/opt/jdk/bin"

### 5. Add source code to server directory 
COPY . /server

### 6. install requirements and run the app
CMD (cd /server; python3 setup.py install; python3 app.py;)
