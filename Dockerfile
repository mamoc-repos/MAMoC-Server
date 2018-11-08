### 1. Get Linux
FROM alpine:3.8
 # Default to UTF-8 file.encoding
ENV LANG C.UTF-8
 # add a simple script that can auto-detect the appropriate JAVA_HOME value
# based on whether the JDK or only the JRE is installed
RUN { \
        echo '#!/bin/sh'; \
        echo 'set -e'; \
        echo; \
        echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \
    } > /usr/local/bin/docker-java-home \
    && chmod +x /usr/local/bin/docker-java-home
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk
ENV PATH $PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin
 ENV JAVA_VERSION 8u181
ENV JAVA_ALPINE_VERSION 8.181.13-r0
 RUN set -x \
    && apk add --no-cache \
        openjdk8="$JAVA_ALPINE_VERSION" \
    && [ "$JAVA_HOME" = "$(docker-java-home)" ]
 ### 2. Get Java via the package manager
# RUN apk update \
# && apk upgrade \
# && apk add --no-cache bash \
# && apk add --no-cache --virtual=build-dependencies unzip \
# && apk add --no-cache curl \
# && apk add --no-cache openjdk8-jre \
# && apk add --no-cache 
 ### 3. Get Python, PIP
 RUN apk add --no-cache python3 \
&& python3 -m ensurepip \
&& pip3 install --upgrade pip setuptools \
&& rm -r /usr/lib/python*/ensurepip && \
if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
rm -r /root/.cache
 ### 4. Set JAVA_HOME
ENV JAVA_HOME="/usr/lib/jvm/java-1.8-openjdk"
 ### 5. Add server code and install 
 ADD . /server
CMD (cd /server; python setup.py install; python app.py;)
