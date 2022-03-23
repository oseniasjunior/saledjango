from celery import shared_task

from core import models, actions, helpers


@shared_task(queue='default')
def save_log_file(state_id: int):
    try:
        state = models.State.objects.get(pk=state_id)
        actions.StateActions.save_log_file(state=state)
    except models.State.DoesNotExist:
        pass


@shared_task(queue='default')
def send_message():
    helpers.send_channel_message('chat', {'message': 'Tarefa periodica'})
