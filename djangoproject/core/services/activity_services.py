from core.models import ActionLog

__author__ = 'tony'


def get_latest_activity(project_id, offset):
    query = ActionLog.objects.all()
    if project_id:
        query = query.filter(project__id=project_id)
    query = query.order_by('-creationDate')
    return query[offset: offset + 10], query.count()
