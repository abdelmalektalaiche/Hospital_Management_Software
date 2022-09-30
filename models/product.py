from odoo import models, fields, api


class ProductTemplate(models.Model):
     _inherit = "product.template"

     type = fields.Selection(selection_add=[
          ('test', 'Test'), ('service',)
          ], tracking=True, ondelete={'test': 'cascade'})
     