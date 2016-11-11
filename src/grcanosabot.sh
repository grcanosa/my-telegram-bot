#!/bin/sh
#
# Put this file in /usr/local/etc/rc.d/btsync.sh

case "$1" in

stop)
    echo "Stop BitTorrent Sync..."
    kill "`cat /tmp/grcanosabot.pid`"
    kill "`cat /tmp/grcanosabot.pid`"
    ;;
start)  
    /volume1/misc/gitproyects/grcanosabot/grcanosabot.py &
    echo $! > /tmp/grcanosabot.pid
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