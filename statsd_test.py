#!/usr/bin/env python

from statsd_to_logstash import Server

srvr = Server(debug=True)
srvr.serve()
