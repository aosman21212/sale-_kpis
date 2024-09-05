{
    'name': 'Sales KPI Management',
    'version': '1.0',
    'summary': 'Manage Sales KPIs, Charts, Calculations, and Dashboards',
    'category': 'Sales',
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/sales_kpi_views.xml',
        'views/sales_kpi_menus.xml',
        'data/sales_kpi_data.xml',
    ],
    'installable': True,
    'application': True,
}
