from odoo import models, fields, api


class SaleOrder(models.Model):
     _inherit = "sale.order"

     sale_description = fields.Char(string='Sale Description')
     