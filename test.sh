#!/bin/bash
http --json POST http://localhost:8000/api/users/ user:='{"username":"intey"}' &>/dev/null
http --json POST http://localhost:8000/api/users/ user:='{"username":"dobby"}' &>/dev/null
http --json POST http://localhost:8000/api/users/1/meets/ meets:='[{"date": "2018-11-11", "timeRange": "18:00-23:00"}]'
http --json POST http://localhost:8000/api/users/1/meets/ meets:='[{"date": "2018-11-10", "timeRange": "17:00-22:00"}]'
http --json GET http://localhost:8000/api/users/1/meets/
