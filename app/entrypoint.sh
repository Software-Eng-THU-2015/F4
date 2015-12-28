#!/bin/bash
set -e
sysctl -w net.core.somaxconn=65535
cd /usr/src/app
exec "$@"
