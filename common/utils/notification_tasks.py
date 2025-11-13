import logging
from django.db import connection
from django.contrib.auth import get_user_model
from panel.Notification.models import Notification

User = get_user_model()
logger = logging.getLogger(__name__)

def send_broadcast_notification_thread(text, link=None):
    try:
        connection.close()
        user_ids_qs = User.objects.filter(is_active=True).values_list('id', flat=True)
        total_users = user_ids_qs.count()
        if total_users == 0:
            logger.info("Broadcast (Thread): No active users found.")
            return

        batch_size = 1000
        notifications_list = []

        for user_id in user_ids_qs.iterator():
            notifications_list.append(
                Notification(user_id=user_id, text=text, link=link)
            )

            if len(notifications_list) >= batch_size:
                Notification.objects.bulk_create(notifications_list, ignore_conflicts=True)
                notifications_list = []

        if notifications_list:
            Notification.objects.bulk_create(notifications_list, ignore_conflicts=True)

        logger.info(f"Broadcast (Thread): Successfully sent to {total_users} users.")

    except Exception as e:
        logger.error(f"Broadcast (Thread) Failed: {str(e)}")
    
    finally:
        connection.close()