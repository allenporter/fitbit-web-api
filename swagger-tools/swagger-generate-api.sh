#!/bin/bash

java -jar ./swagger-tools/swagger-codegen-cli.jar generate \
   -i https://dev.fitbit.com/build/reference/web-api/explore/fitbit-web-api-swagger.json \
   -l python \
   -o . \
   -DpackageName=fitbit_web_api \
   --library asyncio

poetry add $( cat requirements.txt | awk '{print $1;}' )
