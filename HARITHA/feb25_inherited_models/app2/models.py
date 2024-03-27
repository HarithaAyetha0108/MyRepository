from django.db import models
from app1.models import UserProfile

class ProxyUserProfile(UserProfile):
    class Meta:
        proxy=True
    
    def check_pancard(self):
        return self.pancard.upper()