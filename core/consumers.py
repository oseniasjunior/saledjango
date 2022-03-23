from urllib import parse

from channels.generic.websocket import AsyncJsonWebsocketConsumer


class ConsumerBase(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add(self.get_group_name(), self.channel_name)

    def get_query_params(self):
        query_string = self.scope['query_string'].decode()
        return dict(parse.parse_qsl(query_string))

    def get_group_name(self):
        raise NotImplementedError('Deve ser implementado pela subclasse')

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.get_group_name(), self.channel_name)

    async def group_message(self, event):
        await self.send_json(content=event['content'])


class ChatConsumer(ConsumerBase):

    def get_group_name(self):
        return 'chat'

    async def receive_json(self, content, **kwargs):
        print('rebeu a mensagem')
        print(content)
        content['user'] = self.get_query_params()['user']
        await self.channel_layer.group_send(
            self.get_group_name(),
            {'type': 'group.message', 'content': content}
        )
