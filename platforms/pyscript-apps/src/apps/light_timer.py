@service
def light_timer(entity_id: str):
    log.info(entity_id)
    s = state.get(entity_id)
    log.info(s)
