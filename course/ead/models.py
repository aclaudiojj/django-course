from django.db import models


class EadManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(models.Q(name__icontains=query) | models.Q(description__icontains=query))


class Ead(models.Model):

    name = models.CharField('name', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição simples', blank=True)
    about = models.TextField('Sobre o curso', blank=True)
    start_date = models.DateField('Data de Início', blank=True, null=True)
    image = models.ImageField(upload_to='ead/images', verbose_name='Imagem', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = EadManager()

    # from course.ead.models import Ead
    # ead = Ead()
    # ead.name = "Claudio"
    # ead.slug = "claudio"
    # ead.save()
    # ead.delete()

    # eads = Ead.objects.all()
    # eads = Ead.objects.filter(name="claudio").filter(slug="claudio")
    # eads = Ead.objects.filter(name__iexact="claudio")
    # eads = Ead.objects.filter(name__icontains="Krau")
    # - fields lookups -

    # @models.permalink
    def get_absolute_url(self):
        return '/ead/%s' % self.slug

    def __str__(self):
        return self.name

    # class Meta:
    #     verbose_name = 'EAD'
    #     verbose_name_plural = 'EADs'
    #     ordering = ['name']
    #     ordering = ['-name']
