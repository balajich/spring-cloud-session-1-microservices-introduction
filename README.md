# Spring Cloud Microservices Hello World Application
In this tutorial we are going build two microservices applications  and expose they service via gateway. Users access the services using gateway.

- Steps
    - Run employee-api service on 9090. Where it takes employee id and returns employee name.
    - Run payroll-api service on 9050. Where it takes employee id and returns employee salary.
    - Registry (Eureka Server) is running on port 8761 where the microservices employee-api, payroll-api ,gateway services registers to registry.
    - When employee-api,payroll-api  servers starts on their respective ports  9090 and 9050 registers they register with Eureka Server.
    - Spring Cloud Gateway (Spring Cloud load balancer) runs on port 8080
    - Gateway discovers the employee-api, payroll-api by contacting Registry
    - Spring Cloud gateway uses Spring Cloud Load Balancer and routes all the requests that are coming on 8080 to respective application instances.
# Source Code 
    git clone https://github.com/balajich/spring-cloud-microservices-hello-world.git
# Video
[![Spring Cloud LoadBalancer](https://img.youtube.com/vi/8HQR6GdtI9o/0.jpg)](https://www.youtube.com/watch?v=8HQR6GdtI9o)
- https://youtu.be/8HQR6GdtI9o
# Architecture
![architecture](architecture.png "architecture")
# Prerequisite
- JDK 1.8 or above
- Apache Maven 3.6.3 or above
# Clean and Build
    mvn clean install
# Running components
- Registry: ``` java -jar .\registry\target\registry-0.0.1-SNAPSHOT.jar ```
- Employee API: ``` java -jar .\employee-api\target\employee-api-0.0.1-SNAPSHOT.jar ```
- Payroll API: ``` java -jar .\payroll-api\target\payroll-api-0.0.1-SNAPSHOT.jar ```
- Gateway: ```java -jar .\gateway\target\gateway-0.0.1-SNAPSHOT.jar ``` 

# Using curl to test environment
**Note I am running CURL on windows, if you have any issue. Please use postman client, its collection is available 
at spring-cloud-microservices-hello-world.postman_collection.json**
- Access employee api directly: ``` curl -s -L  http://localhost:9090/employee/100 ```
- Access payroll api directly: ``` curl -s -L  http://localhost:9050/payroll/100 ```
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
# Next Tutorial
https://github.com/balajich/spring-cloud-microservices-hello-world-dynamic-ports