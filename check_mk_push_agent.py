#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
import time

import requests

if __name__ == '__main__':
    url = os.environ["URL"]
    token = os.environ["TOKEN"]

    while True:
        try:
            agent_data = subprocess.check_output(['/usr/bin/check_mk_agent'])
            resp = requests.post(
                '{}/push/{}'.format(url, token),
                data=agent_data
            )
            if resp.status_code != 200:
                raise RuntimeError('Server responded with '+str(resp))
        except Exception as e:
            print e
        time.sleep(45)
