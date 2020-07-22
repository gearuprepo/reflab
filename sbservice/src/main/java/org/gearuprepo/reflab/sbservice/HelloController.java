package org.gearuprepo.reflab.sbservice;

import java.net.http.HttpHeaders;

import org.springframework.http.HttpEntity;
import org.springframework.http.HttpMethod;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

@RestController
class HelloController {

    //Service Discovery using Native k8s service
    private String server = "http://sbservice2svc:8080/sbservice2/hello";
    private RestTemplate rest;
    private HttpHeaders headers;
    private HttpStatus status;
  
    public HelloController() {
      this.rest = new RestTemplate();
    }

    @GetMapping("/hello")
    public String getHello() {
        return "Hello from Spring boot - Sbservice1";
    }

    @GetMapping("/route2")
    public String get() {
        HttpEntity<String> requestEntity = new HttpEntity<String>("");
        ResponseEntity<String> responseEntity = rest.exchange(server, HttpMethod.GET, requestEntity, String.class);
        //this.setStatus(responseEntity.getStatusCode());
        return responseEntity.getBody();
      }
      
}