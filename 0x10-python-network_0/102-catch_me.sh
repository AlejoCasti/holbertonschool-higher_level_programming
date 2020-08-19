#!/bin/bash
#Send a POST request with some parameters
curl -s -X PUT -d Allow=GET -L 0.0.0.0:5000/catch_me -d user_id=98 -H "Origin: HolbertonSchool"
