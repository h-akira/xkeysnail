#!/bin/sh
#
# restart.sh
# Created:      Oct, 16, 2022 02:49:24 by h-akira
set -eu

if [ -e "$(which xkeysnail)" ]; then
  PID=`ps --no-heading -C xkeysnail -o pid | tr -d ' '`
  if [ -n "$PID" ]; then
    echo "Stop xkeysnail (kill PID: $PID)"
    sudo kill $PID
  fi
  echo "Start xkeysnai"
  if [ $# = 1 ]; then
    sudo xkeysnail -q $1 &
  elif [ $# = 0 ]; then
    sudo xkeysnail -q $(dirname $0)/../config.py &
  else
    echo "Too manny arguments"
  fi
else
  echo "Please install xkeysnail by 'sudo pip3 install xkeysnasil'"
fi
