print("Hello World")

'''
Python API for Jenkins

Examples::

    j = jenkins.Jenkins('http://3.89.99.228:8080/', 'admin', 'abc123')
    j.get_jobs()
    j.create_job('empty', jenkins.EMPTY_CONFIG_XML)
    j.disable_job('empty')
    j.copy_job('empty', 'empty_copy')
    j.enable_job('empty_copy')
    j.reconfig_job('empty_copy', jenkins.RECONFIG_XML)
    j.delete_job('empty')
    j.delete_job('empty_copy')
    # build a parameterized job
    j.build_job('api-test', {'param1': 'test value 1', 'param2': 'test value 2'})
'''

import sys
import urllib2
import urllib
import base64
import traceback
import json
import httplib


NODE_INFO   = 'computer/%(name)s/api/json?depth=0'



def get_node_info(self, name):
    '''
    Get node information dictionary
    :param name: Node name, ``str``
    :returns: Dictionary of node info, ``dict``
    '''
    try:
        response = self.jenkins_open(urllib2.Request(self.server + NODE_INFO%locals()))
        if response:
            return json.loads(response)
        else:
            raise JenkinsException('node[%s] does not exist'%name)
    except urllib2.HTTPError:
        raise JenkinsException('node[%s] does not exist'%name)
    except ValueError:
        raise JenkinsException("Could not parse JSON info for node[%s]"%name)
