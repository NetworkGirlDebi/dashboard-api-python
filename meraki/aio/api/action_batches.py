class AsyncActionBatches:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def createOrganizationActionBatch(self, organizationId: str, actions: list, **kwargs):
        """
        **Create an action batch**
        https://developer.cisco.com/docs/meraki-api-v0/#!create-organization-action-batch
        
        - organizationId (string)
        - actions (array): A set of changes to make as part of this action (<a href='https://developer.cisco.com/meraki/api/#/rest/guides/action-batches/'>more details</a>)
        - confirmed (boolean): Set to true for immediate execution. Set to false if the action should be previewed before executing. This property cannot be unset once it is true. Defaults to false.
        - synchronous (boolean): Set to true to force the batch to run synchronous. There can be at most 20 actions in synchronous batch. Defaults to false.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Action batches'],
            'operation': 'createOrganizationActionBatch',
        }
        resource = f'/organizations/{organizationId}/actionBatches'

        body_params = ['confirmed', 'synchronous', 'actions']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)

    async def getOrganizationActionBatches(self, organizationId: str):
        """
        **Return the list of action batches in the organization**
        https://developer.cisco.com/docs/meraki-api-v0/#!get-organization-action-batches
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['Action batches'],
            'operation': 'getOrganizationActionBatches',
        }
        resource = f'/organizations/{organizationId}/actionBatches'

        return await self._session.get(metadata, resource)

    async def getOrganizationActionBatch(self, organizationId: str, actionBatchId: str):
        """
        **Return an action batch**
        https://developer.cisco.com/docs/meraki-api-v0/#!get-organization-action-batch
        
        - organizationId (string)
        - actionBatchId (string)
        """

        metadata = {
            'tags': ['Action batches'],
            'operation': 'getOrganizationActionBatch',
        }
        resource = f'/organizations/{organizationId}/actionBatches/{actionBatchId}'

        return await self._session.get(metadata, resource)

    async def deleteOrganizationActionBatch(self, organizationId: str, actionBatchId: str):
        """
        **Delete an action batch**
        https://developer.cisco.com/docs/meraki-api-v0/#!delete-organization-action-batch
        
        - organizationId (string)
        - actionBatchId (string)
        """

        metadata = {
            'tags': ['Action batches'],
            'operation': 'deleteOrganizationActionBatch',
        }
        resource = f'/organizations/{organizationId}/actionBatches/{actionBatchId}'

        return await self._session.delete(metadata, resource)

    async def updateOrganizationActionBatch(self, organizationId: str, actionBatchId: str, **kwargs):
        """
        **Update an action batch**
        https://developer.cisco.com/docs/meraki-api-v0/#!update-organization-action-batch
        
        - organizationId (string)
        - actionBatchId (string)
        - confirmed (boolean): A boolean representing whether or not the batch has been confirmed. This property cannot be unset once it is true.
        - synchronous (boolean): Set to true to force the batch to run synchronous. There can be at most 20 actions in synchronous batch.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Action batches'],
            'operation': 'updateOrganizationActionBatch',
        }
        resource = f'/organizations/{organizationId}/actionBatches/{actionBatchId}'

        body_params = ['confirmed', 'synchronous']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

