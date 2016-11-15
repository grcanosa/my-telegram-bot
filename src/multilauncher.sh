#!/bin/sh
#
# Put this file in /usr/local/etc/rc.d/btsync.sh

case "$1" in

stop)
    echo "Stop Bots"
    killall -9 multilauncher.py
    #kill "`cat /tmp/telegrambots.pid`"
    ;;
start)
    symlink=$(readlink -f "$0")
	  path=$(dirname $symlink)
	  echo $path
	  $path/multilauncher.py &
    #echo $! > /tmp/telegrambots.pid
    ;;
restart)
    $0 stop
    sleep 1
    $0 start
    ;;
*)
    echo "usage: $0 { start | stop | restart }" >&2
        exit 1
        ;;
esac
