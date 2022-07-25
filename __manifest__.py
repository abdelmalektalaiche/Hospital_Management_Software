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
        'views/patient.xml',
        'security/ir.model.access.csv',
        'views/sale.xml'
        ],
    'demo' : [],
    'qweb' : [],
    'installable':True,
    'application':True,
    'auto-install':False,
    
}