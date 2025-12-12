import collections

from stubs.pyscript_builtins import log, service, task
from stubs.pyscript_generated import light


class LightTimer:
    task = None

    def run(self, entity_id: str, new_state: str):
        # whenever state switched we will not continue with an existing timer task:
        if self.task:
            task.cancel(self.task)
            self.task = None

        if new_state == 'on':
            self.task = task.create(LightTimer.turn_off_after, self, entity_id)

    def turn_off_after(self, entity_id: str):
        task.sleep(5)
        log.info('Timer expired.')
        light.turn_off(entity_id=entity_id)
        self.task = None


light_timer_entity = collections.defaultdict(LightTimer)


@service
def light_timer(entity_id: str, new_state: str):
    obj = light_timer_entity[entity_id]
    LightTimer.run(obj, entity_id, new_state)
