#!/bin/sh
#
# Put this file in /usr/local/etc/rc.d/btsync.sh

case "$1" in

stop)
    echo "Stop BitTorrent Sync..."
    kill "`cat /tmp/grcanosabot.pid`"
    kill "`cat /tmp/grcanosabot.pid`"
	kill "`cat /tmp/zalamerobot.pid`"
	kill "`cat /tmp/zalamerobot.pid`"
    ;;
start)  
    ./grcanosabot.py &
    echo $! > /tmp/grcanosabot.pid
	./zalamerobot.py &
	echo $! > /tmp/zalamerobot.pid
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
