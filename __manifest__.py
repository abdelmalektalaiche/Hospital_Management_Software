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
        'hr'
        ],
    'data' : [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/patient_view.xml',
        'views/patient_gender_view.xml',
        'views/kids_view.xml',
        'views/appointment_view.xml',
        'views/sale.xml'
        ],
    'demo' : [],
    'qweb' : [],
    'installable':True,
    'application':True,
    'auto-install':False,
    
}