from django.contrib.auth.models import User # Modello User
from django.db.models.signals import post_save # che invierà QUESTO SEGNALE quando viene salvata
from django.dispatch import receiver # abbiamo quindi questo decoratore Reciver che andrà a captare questo segnale
from profiles.models import Profile # e questo è il modello che verrà instanziato al segnale ricevuto dal sender=User

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print("Created: ", created)
    if created:
        Profile.objects.create(user=instance)