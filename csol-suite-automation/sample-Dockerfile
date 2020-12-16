FROM maven:3.6.3-jdk-8
RUN mkdir -p /usr/src/app
EXPOSE 8080
WORKDIR /usr/src/app
ADD . /usr/src/app
RUN mvn clean test