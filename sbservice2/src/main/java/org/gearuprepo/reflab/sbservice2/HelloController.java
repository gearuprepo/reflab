package org.gearuprepo.reflab.sbservice2;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
class HelloController {
    @GetMapping("/hello")
    public String getHello() {
        return "Hello from Spring boot - Sbservice2";
    }
}