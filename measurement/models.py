from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=250, verbose_name='Name')
    description = models.CharField(max_length=250, blank=True, verbose_name='Description')
    image = models.ImageField(max_length=30, null=True)

    class Meta:
        verbose_name = 'Sensor'
        verbose_name_plural = 'Sensors'
        ordering = ['name']

    def __str__(self):
        return '{0}_{1}'.format(self.name, self.description)


class Measurement(models.Model):
    temperature = models.DecimalField(max_digits=3, decimal_places=1)
    created_at = models.DateTimeField(auto_now=True)
    sensor = models.ForeignKey(to=Sensor, blank=False, on_delete=models.CASCADE,
                               related_name='measurements')

    class Meta:
        verbose_name = 'measurement'
        verbose_name_plural = 'measurements'
        ordering = ['created_at']

    def __str__(self):
        return '{0}_{1}_{2}'.format(self.sensor, self.temperature, self.created_at)
