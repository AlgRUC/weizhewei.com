#!/bin/bash

docker compose run jekyll bundle exec jekyll build
purgecss -c purgecss.config.js