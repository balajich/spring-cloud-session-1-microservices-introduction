# Spring Cloud Session1 Microservices Introduction
In this tutorial we are going build three microservices and expose their service via gateway. User will
access the services via gateway. Two services (employee-api,payroll-api) is developed in Java and insurance-api is 
developed in python. All the services are simple http REST apis.

Overview
- Run employee-api service on 9000. Where it takes employee id and returns employee name.
- Run payroll-api service on 9010. Where it takes employee id and returns employee salary.
- Run insurance-api service on 9020. Where it takes employee id and returns employee sum insured.
- Run Gateway service on 8080 and reverse proxy requests to all the services (employee-api,payroll-api,insurance-api)
- Spring Cloud load balancer (Client side load balancing) component in Spring Cloud Gateway acts as reverse proxypective application instances.
 
What is covered ?
- Develop restapi microservices in Java using springboot 
- Develop restapi microservices in Python using flask
- Develop ApiGateway micorservice in Java using Spring Cloud

# Source Code 
``` git clone https://github.com/balajich/spring-cloud-session-1-microservices-introduction.git ```
# Video
[![Spring Cloud LoadBalancer](https://img.youtube.com/vi/8HQR6GdtI9o/0.jpg)](https://www.youtube.com/watch?v=8HQR6GdtI9o)
- https://youtu.be/8HQR6GdtI9o
# Architecture
![architecture](architecture.png "architecture")
# Prerequisite
- JDK 1.8 or above
- Apache Maven 3.6.3 or above
- Python 3.7.8 or above
# Clean and Build
- Java
    - ``` cd spring-cloud-session-1-microservices-introduction ``` 
    - ``` mvn clean install ```
- Python
    - ``` cd \spring-cloud-session-1-microservices-introduction\insurance-api ```
    - ```  pipenv install ``` 
 
 **Note: Maven is build and dependency tool for Java where as Pipenv is dependency tool for Python**
 
# Running components
- Registry: ``` java -jar .\registry\target\registry-0.0.1-SNAPSHOT.jar ```
- Employee API: ``` java -jar .\employee-api\target\employee-api-0.0.1-SNAPSHOT.jar ```
- Payroll API: ``` java -jar .\payroll-api\target\payroll-api-0.0.1-SNAPSHOT.jar ```
- Gateway: ```java -jar .\gateway\target\gateway-0.0.1-SNAPSHOT.jar ``` 

# Using curl to test environment
**Note I am running CURL on windows, if you have any issue. Please use postman client, its collection is available 
at spring-cloud-microservices-hello-world.postman_collection.json**
- Access employee api directly: ``` curl -s -L  http://localhost:9000/employee/100 ```
- Access payroll api directly: ``` curl -s -L  http://localhost:9010/payroll/100 ```
- Access employee api via gateway: ``` curl -s -L  http://localhost:8080/employee/100 ```
- Access payroll api via gateway: ``` curl -s -L  http://localhost:8080/payroll/100 ```

**Note: Users will not access microservices (employee-api,payroll-api) directly. This will always access via gateway**
# Scale up restapi instances
Start two new instances of employee-api , payroll-api to handle increasing load 
- Employee API instance 2: ``` java -jar '-Dserver.port=9091' .\employee-api\target\employee-api-0.0.1-SNAPSHOT.jar ```
- Payroll API instance 2: ``` java -jar '-Dserver.port=9051' .\payroll-api\target\payroll-api-0.0.1-SNAPSHOT.jar ```
**Notice new instances are running on port 9091,9051**
# Registry UI
Use Eureka Service registry UI to view all the micro service instances http://localhost:8761
![EurekaServiceRegistry](EurekaServiceRegistry.PNG "EurekaServiceRegistry")
# Next Steps
- Enhance existing application to run employee-api and payroll-api on dynamic ports.
- Ideally we will not care on which ports employee-api and payroll-api is running because we don't access the api directly, We always use gateway.
# References
- https://howtodoinjava.com/microservices/microservices-definition-principles-benefits/
- https://en.wikipedia.org/wiki/Microservices
# Next Tutorial
https://github.com/balajich/spring-cloud-microservices-hello-world-dynamic-ports