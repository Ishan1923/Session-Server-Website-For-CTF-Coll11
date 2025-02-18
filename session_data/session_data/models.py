from django.db import models 

class SessionData(models.Model):
    team_name = models.CharField(max_length=255, unique=True)
    team_score = models.IntegerField()
    questions_answered = models.JSONField(default = list)

    def __str__(self):
        return self.team_name
    
    class Meta:
        db_table = "session_data_sessiondata"