from datetime import datetime


def soft_delete(instance, session):
    instance.deleted_at = datetime.utcnow()
    session.add(instance)
    session.commit()
