#!/bin/bash
#Show all http methods supported
curl -sI $1 | grep Allow: | cut -b 8-
