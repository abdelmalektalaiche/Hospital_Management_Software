from odoo import models, fields, api


class HospitalPatient(models.Model):
     _name = 'hospital.patient'
     _inherit = ["mail.thread","mail.activity.mixin"]
     _description = 'Hospital Patient'

     name = fields.Char(string='Name', tracking=True, required=True)
     age = fields.Integer(string='Age', tracking=True)
     gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')], required=True, tracking=True, default='male')
     note = fields.Text(string='Description', tracking=True)
     state = fields.Selection([('draft','Draft'), ('confirm','confirmed'), ('done','Done'), ('cancel','Cancelled')], default='draft', tracking=True, string='status')
     responsible_id = fields.Many2one('res.partner', string='Responsible') 
     
     def action_confirm(self):
          self.state = 'confirm'
          
     def action_done(self):
          self.state = 'done'
          
     def action_draft(self):
          self.state = 'draft'
          
     def action_cancel(self):
          self.state = 'cancel'
          
     @api.model 
     def create(self, vals):
          if not vals.get('note'):
               vals['note'] = 'New Patient'
          res = super(HospitalPatient, self).create(vals)
          return res