class UplinkSettings(object):
    def __init__(self, session):
        super(UplinkSettings, self).__init__()
        self._session = session
    
    def getNetworkUplinkSettings(self, networkId: str):
        """
        **Returns the uplink settings for your MX network.**
        https://developer.cisco.com/docs/meraki-api-v0/#!get-network-uplink-settings
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Uplink settings'],
            'operation': 'getNetworkUplinkSettings',
        }
        resource = f'/networks/{networkId}/uplinkSettings'

        return self._session.get(metadata, resource)

    def updateNetworkUplinkSettings(self, networkId: str, **kwargs):
        """
        **Updates the uplink settings for your MX network.**
        https://developer.cisco.com/docs/meraki-api-v0/#!update-network-uplink-settings
        
        - networkId (string)
        - bandwidthLimits (object): A mapping of uplinks to their bandwidth settings (be sure to check which uplinks are supported for your network)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Uplink settings'],
            'operation': 'updateNetworkUplinkSettings',
        }
        resource = f'/networks/{networkId}/uplinkSettings'

        body_params = ['bandwidthLimits']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

