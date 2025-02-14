#!/bin/bash

sudo rm -r _site
docker compose run jekyll bundle exec jekyll build
purgecss -c purgecss.config.js