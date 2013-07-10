#!/bin/bash

set -x
cd ../..
# reset remote database
/usr/local/heroku/bin/heroku pg:reset DATABASE_URL --confirm oquize

# create tables
scripts/heroku/sync.expect

# add questions into the database
scripts/heroku/dbadd.expect
