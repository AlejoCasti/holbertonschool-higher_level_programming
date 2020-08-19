#!/bin/bash
#Send a POST request with some parameters
curl -s -X PUT -d "Allow=GET" -L $1 -d "user_id=98" -H "Origin: HolbertonSchool"
