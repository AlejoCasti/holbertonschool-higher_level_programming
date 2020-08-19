#!/bin/bash
#get size of the body from header
curl -Is $1 | grep Content-Length: | cut -b 17-
