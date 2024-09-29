#!/usr/bin/env bash
set -o errexit
set -o nounset
set -o pipefail

# Make sure to...
#
# Install doctl
#  `brew install doctl`
#
# Authenticate:
#  `doctl auth init` (paste in docker API key with credential access)

doctl registry login
docker build --platform linux/amd64 -t calcapiamd .
docker tag calcapiamd registry.digitalocean.com/spacerat/calcapiamd
docker push registry.digitalocean.com/spacerat/calcapiamd
