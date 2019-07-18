from django.db import models

class Category(models.Model):
    STATUS = (
        ('active', 'Ativo'),
        ('draft', 'Rascunho')
    )
    name = models.CharField(max_length=250, verbose_name="Categoría")
    slug = models.SlugField()
    image = models.ImageField(upload_to='category_image', blank=True)
    created_at = models.DateField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateField(auto_now=True, verbose_name="Data de Alteração")
    status = models.CharField(max_length=15, choices=STATUS)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Categoria'
        verbose_name_plural = u'Categorias'


class SubCategory(models.Model):
    STATUS = (
        ('active', 'Ativo'),
        ('draft', 'Rascunho')
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, verbose_name="Nome do comissão")
    sigla = models.CharField(max_length=10, verbose_name="Sigla ")
    created_at = models.DateField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateField(auto_now=True,  verbose_name="Data de Alteração")
    status = models.CharField(max_length=15, choices=STATUS)

    def __str__(self):
        return self.sigla

    class Meta:
        verbose_name = u'Tipo de Categoria'
        verbose_name_plural = u'Tipo de Categorias'



class SubCategoryItem(models.Model):
    STATUS = (
        ('active', 'Ativo'),
        ('draft', 'Rascunho')
    )
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=250,  verbose_name="Titulo do Formulário")
    slug = models.SlugField()
    link= models.URLField(max_length=250,  verbose_name="Endereço do formulário")
    created_at = models.DateField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateField(auto_now=True,  verbose_name="Data de Alteração")
    status = models.CharField(max_length=15, choices=STATUS)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'Formulário'
        verbose_name_plural = u'Formulários'
