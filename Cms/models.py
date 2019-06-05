from django.db import models

# Create your models here.
class BaseTable(models.Model):
    """
    公共字段列
    """

    class Meta:
        abstract = True
        verbose_name = "公共字段表"
        db_table = 'BaseTable'

    id = models.AutoField('主键', primary_key=True, )
    name = models.CharField('名称',max_length=50,null=False)
    description = models.CharField('描述',max_length=200,null=False)
    leader = models.CharField('负责人',max_length=50,null=False)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

class Product(BaseTable):
    """
    产品信息表
    """
    class Meta:
        verbose_name = "产品信息"
        db_table = "Product"

    finish_time = models.DateTimeField('完成产品时间',auto_now=True)


class Project(BaseTable):
    """
    项目表
    """
    class Meta:
        verbose_name = "项目表"
        db_table = "Project"
    product_id = models.ForeignKey(Product,related_name='project_product',null=True,on_delete=models.SET_NULL)
    finish_time = models.DateTimeField('完成产品时间',auto_now=True)

class Module(BaseTable):
    """
    模块表
    """
    class Meta:
        verbose_name = "模块表"
        db_table = "Module"

    project_id = models.ForeignKey(Project,related_name='module_project',null=True,on_delete=models.SET_NULL)
    finish_time = models.DateTimeField('完成模块时间',auto_now=True)

class Case(BaseTable):
    """
    用例表
    """
    class Meta:
        verbose_name = "用例表"
        db_table = "Case"
    case_choice = (
        (1,"UI用例"),
        (2,"接口用例"),
        (3,"app用例")
    )

    module_id = models.ForeignKey(Module,related_name='case_module',null=True,on_delete=models.SET_NULL)
    case_group = models.IntegerField('用例所属组',choices=case_choice,)
    delete_time = models.DateTimeField('用例删除时间',auto_now=True)

