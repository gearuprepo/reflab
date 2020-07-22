# Getting Started

### Reference Documentation
For further reference, please consider the following sections:

* [Official Apache Maven documentation](https://maven.apache.org/guides/index.html)
* [Spring Boot Maven Plugin Reference Guide](https://docs.spring.io/spring-boot/docs/2.3.1.RELEASE/maven-plugin/reference/html/)
* [Create an OCI image](https://docs.spring.io/spring-boot/docs/2.3.1.RELEASE/maven-plugin/reference/html/#build-image)
* [Spring Web](https://docs.spring.io/spring-boot/docs/2.3.1.RELEASE/reference/htmlsingle/#boot-features-developing-web-applications)

### Guides
The following guides illustrate how to use some features concretely:

* [Building a RESTful Web Service](https://spring.io/guides/gs/rest-service/)
* [Serving Web Content with Spring MVC](https://spring.io/guides/gs/serving-web-content/)
* [Building REST services with Spring](https://spring.io/guides/tutorials/bookmarks/)

## Docker commands
Build for prod before executing docker
docker build -t sbserviceimg .
docker run -it --rm -p 8080:8080 sbserviceimg

## For pointing to minikubes docker repo
eval $(minikube docker-env)
Unsetting - eval $(minikube docker-env -u)

## Kube get
kubectl get all -o wide
## Kube Create
Kubectl create -f manifest.yaml
For recording deployment (rolling strategy) kubectl create -f manifest.yaml --record
## Kube Delete
Kubectl delete -f manifest.yaml

## Kube service - Let’s take a look at the endpoint. It holds the list of Pods that should receive requests.
kubectl get -f svc/<svc>
kubectl get ep <svc> -o yaml

## To Ping the service endpoint
IP=$(minikube ip)
PORT=$(kubectl get svc sbservicesvc -o jsonpath="{.spec.ports[0].nodePort}")
curl -i "http://$IP:$PORT/sbservice/hello"

## Rollout describe
kubectl rollout status -w -f manifest.yaml

## Ingress related
minikube addons list
minikube addons enable ingress
kubectl get pods -n kube-system | grep ingress
curl -i "http://$IP/healthz"
Single Service Ingress
http://$IPING/sbservice/hello
http://$IPING/sbservice/route2