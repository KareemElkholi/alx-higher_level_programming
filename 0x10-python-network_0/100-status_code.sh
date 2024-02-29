#!/bin/bash
# displays only the status code of the response
curl -so /dev/null -w "%{response_code}" "$1"
