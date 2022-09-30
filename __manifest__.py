{
    
    'name' : 'Hospital Management',
    'version': '0.1',
    'summary' : 'Hospital Management Software',
    'sequence' : 40,
    'description' : """Hospital Management Software""",
    'author': "TALAICHE Abdelmalek",
    'website': "http://www.ESI.dz",
    'category': 'Productivity',
    'depends' : [
        'sale',
        'mail',
        'hr',
        'report_xlsx'
        ],
    'data' : [
        'security/ir.model.access.csv',
        'data/data.xml',
        'wizard/create_appointment_view.xml',
        'wizard/search_appointment_view.xml',
        'wizard/appointment_report_view.xml',
        'wizard/all_patient_report_view.xml',
        'views/patient_view.xml',
        'views/patient_gender_view.xml',
        'views/kids_view.xml',
        'views/appointment_view.xml',
        'views/doctor_view.xml',
        'views/sale.xml',
        'views/partner.xml',
        'report/patient_card.xml',
        'report/appointment_details.xml',
        'report/all_patient_list.xml',
        'report/report.xml'
        ],
    'demo' : [],
    'qweb' : [],
    'installable':True,
    'application':True,
    'auto-install':False,
    
}