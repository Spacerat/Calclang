#!/usr/bin/env bash
set -o errexit
set -o nounset
set -o pipefail

docker build --platform linux/amd64 -t calcapiamd .
docker tag calcapiamd registry.digitalocean.com/spacerat/calcapiamd
docker push registry.digitalocean.com/spacerat/calcapiamd
