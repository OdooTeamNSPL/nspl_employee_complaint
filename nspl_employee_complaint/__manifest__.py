{
    'name': 'Employee Complaint',
    'version': '17.0',
    'summary':
        """
The Employee Complaint module lets employees submit and track complaints within Odoo HR, streamlining issue resolution and promoting transparency. It's ideal for improving workplace communication and formalizing grievance management.
    """,
    'description': """
    ✔ Submit Complaints with Details
    ✔ Complaint Status Tracking
     """,
    'category': 'Employee',
    'sequence': 2,
    'author': 'Namah Softech Private Limited',
    'website': 'https://www.namahsoftech.com/',
    'license': 'OPL-1',
    'price': 17.99,
    'currency': 'USD',
    'support': 'support@namahsoftech.com',
    'contributors': ["Rutik Patil"],
    'depends': ['hr', 'mail', 'base'],
    'data': [
        'security/ir.model.access.csv',
        'views/complaint_type_views.xml',
        'views/complaint_page.xml',
        'views/employee_complaint_views.xml',
    ],
    'images': ['static/description/img/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
