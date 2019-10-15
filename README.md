[![Build Status](https://travis-ci.com/trydirect/registry.svg?branch=master)](https://travis-ci.com/trydirect/registry)
![Docker Stars](https://img.shields.io/docker/stars/trydirect/registry.svg)
![Docker Pulls](https://img.shields.io/docker/pulls/trydirect/registry.svg)
![Docker Automated](https://img.shields.io/docker/cloud/automated/trydirect/registry.svg)
![Docker Build](https://img.shields.io/docker/cloud/build/trydirect/registry.svg)
[![Gitter chat](https://badges.gitter.im/trydirect/community.png)](https://gitter.im/try-direct/community)
# Docker Registry docker-compose v2 

Docker registry with Nginx and Let's Encrypt 

# 
This repo helps to bring up Docker Registry quickly using docker-compose.

**Stack includes**: 
 * Docker registry image: registry:2
 * Web interface docker image: hyper/docker-registry-web:latest
 * Nginx
 

## Installation
Clone project into your work directory:
```sh
$ git clone https://github.com/trydirect/registry.git
```
Bring up docker services:
```sh
$ cd registry
$ docker-compose up -d
```


## Run Tests

```
$ python tests.py 
```


## Quick deployment to cloud
##### Amazon AWS, Digital Ocean, Hetzner and others
[<img src="https://img.shields.io/badge/quick%20deploy-%40try.direct-brightgreen.svg">](https://try.direct/server/user/deploy/InJlZ2lzdHJ5fDZ8MzIi.EIJLoA.-NyS4DE9LucPVr9WaQzHZTnbmvE/)



## Contributing


1. Fork it (<https://github.com/trydirect/registry/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request


## Support Development

Send your PR's, ideas or 

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=2BH8ED2AUU2RL) 


