print("Hello World")
def node_exists(self, name):
        '''
        :param name: Name of Jenkins node, ``str``
        :returns: ``True`` if Jenkins node exists
        '''
        try:
            self.get_node_info(name)
            return True
        except JenkinsException:
            return False
