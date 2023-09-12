#!/bin/sh
#
# Created:      Oct, 16, 2022 02:38:17
set -eu

PID=`ps --no-heading -C xkeysnail -o pid | tr -d ' '`

if [ -n "$PID" ]; then
  sudo kill $PID
  echo "Stopped xkeysnail (kill PID: $PID)"
fi
