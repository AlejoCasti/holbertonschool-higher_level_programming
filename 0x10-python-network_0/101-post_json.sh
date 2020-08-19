#!/bin/bash
#Send a POST request with some parameters
curl -sd "@$2" -H "Content-Type: application/json" -X POST $1
