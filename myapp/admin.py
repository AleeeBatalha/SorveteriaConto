from django.contrib import admin
from myapp import models

# Registre os modelos principais
admin.site.register(models.Embalagem)
admin.site.register(models.TipoSabor)
admin.site.register(models.Sabor)
admin.site.register(models.Cobertura)
admin.site.register(models.Pedido)

# Monta Pote - Adiciona os sabores ao modelo MontaPote usando TabularInline
class SelSaborInline(admin.TabularInline):
    model = models.SelSabor
    extra = 0  # Número de formulários vazios adicionais para adição de novos itens

@admin.register(models.MontaPote)
class MontaPoteAdmin(admin.ModelAdmin):
    inlines = [SelSaborInline]  # Inclui os sabores diretamente na visualização de MontaPote

# Sacola de Itens - Adiciona os potes e pedidos à visualização da SacolaItens
class MontaPoteInline(admin.TabularInline):
    model = models.SacolaItens.potes.through  # Relacionamento muitos-para-muitos entre MontaPote e SacolaItens
    extra = 0  # Número de formulários vazios adicionais

class PedidoInline(admin.StackedInline):
    model = models.Pedido
    extra = 0  # Número de formulários vazios adicionais

@admin.register(models.SacolaItens)
class SacolaItensAdmin(admin.ModelAdmin):
    fields = ('preco',)  # Campos a serem exibidos no modelo SacolaItens
    readonly_fields = ('preco',)  # O campo preço será somente leitura
    inlines = [PedidoInline, MontaPoteInline]  # Adiciona os inlines para Pedido e MontaPote
