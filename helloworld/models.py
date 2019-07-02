from django.db import models


class Counter(models.Model):
    groupno = models.IntegerField(default=0)
    depth = models.IntegerField(default=0)
    orderno = models.IntegerField(default=0)

    def __str__(self):
        return f'Counter({self.groupno}, {self.depth}, {self.orderno})'
