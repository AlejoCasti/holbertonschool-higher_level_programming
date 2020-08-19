#!/bin/bash
#Send a POST request with some parameters
curl -s -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" -X POST $1
