import asyncio

from stubs.pyscript_builtins import log, service, task
from stubs.pyscript_generated import light

task_by_entity: dict[str, asyncio.Task] = {}


def turn_off_light_after(entity_id: str, duration: int):
    log.info('Scheduling to turn of %r after %d minutes.', entity_id, duration)
    task.sleep(duration * 60)
    log.info('Timer expired, turning off %r.', entity_id)
    light.turn_off(entity_id=entity_id)
    del task_by_entity[entity_id]


def run(entity_id: str, new_state: str, duration: int):
    # whenever state switched we will not continue with an existing timer task:
    if entity_task := task_by_entity.get(entity_id):
        log.info('Cancelling timer to turn of %r.', entity_id)
        task.cancel(entity_task)
        del task_by_entity[entity_id]

    if new_state == 'on':
        task_by_entity[entity_id] = task.create(turn_off_light_after, entity_id, duration)


@service
def light_timer(entity_id: str, new_state: str, duration: int):
    run(entity_id, new_state, duration)
