from odoo import models, fields, api



class AllPatientReport(models.AbstractModel):
    _name = 'report.om_hospital.report_all_patient_list'
    _description = 'Patient Report'
    
    @api.model
    def _get_report_values(self, docids, data=None):
        domain = []
        gender = data.get('form_data').get('gender')
        age = data.get('form_data').get('age')
        if gender:
            domain += [('gender', '=', gender)]
        if age != 0:
            domain += [('age', '=', age)]
        docs= self.env['hospital.patient'].search(domain)
        return{
            'docs': docs,
            'email': 'ka_talaiche@esi.dz',
        }
        

class PatientDetailsReport(models.AbstractModel):
    _name = 'report.om_hospital.report_patient_detail'
    _description = 'Patient Details Report'
    
    @api.model
    def _get_report_values(self, docids, data=None):
        docs= self.env['hospital.patient'].search([])
        return{
            'docs': docs,
            'email': 'ka_talaiche@esi.dz',
        }
    