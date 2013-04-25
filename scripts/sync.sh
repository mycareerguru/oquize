#!/bin/bash

set -x
cd ../
rm db.sql
./scripts/sync.expect
./scripts/dbadd.expect
