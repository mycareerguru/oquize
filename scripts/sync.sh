#!/bin/bash

set -x
rm db.sql
./sync.expect
./dbadd.expect
