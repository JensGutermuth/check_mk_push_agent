# Agent component of a push agent setup for check_mk

Run the `check_mk_push_agent.py` script as a daemon, preferably with a process
supervisor such as [supervisord](http://supervisord.org/).

The server component the
[check_mk_push_agent](https://github.com/Delphinator/check_mk_push_agent_server)
repo.

Configuration is done via environment variables:
- `URL`: Url of the server without trailing slash.
- `TOKEN`: Token for this host
