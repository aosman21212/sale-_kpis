from odoo import models, fields

class SalesKPI(models.Model):
    _name = 'sales.kpi'
    _description = 'Sales KPI Data'

    name = fields.Char(string='KPI Name', required=True)
    jan = fields.Float(string='January')
    feb = fields.Float(string='February')
    mar = fields.Float(string='March')
    apr = fields.Float(string='April')
    may = fields.Float(string='May')
    jun = fields.Float(string='June')
    jul = fields.Float(string='July')
    aug = fields.Float(string='August')
    sep = fields.Float(string='September')
    oct = fields.Float(string='October')
    nov = fields.Float(string='November')
    dec = fields.Float(string='December')
    total = fields.Float(string='Total')
    average_deal_size = fields.Float(string='Average Deal Size')
    required_deals = fields.Integer(string='Required Deals')

    chart_ids = fields.One2many('sales.kpi.chart', 'kpi_id', string='Charts')
    calc_ids = fields.One2many('sales.kpi.calc', 'kpi_id', string='Calculations')
    dashboard_ids = fields.One2many('sales.kpi.dashboard', 'kpi_id', string='Dashboards')


class SalesKPIChart(models.Model):
    _name = 'sales.kpi.chart'
    _description = 'Sales KPI Chart Data'

    kpi_id = fields.Many2one('sales.kpi', string='Related KPI', required=True)
    gauge_chart_name = fields.Char(string='Gauge Chart Name')
    min = fields.Float(string='Minimum Value')
    max = fields.Float(string='Maximum Value')
    value = fields.Float(string='Current Value')
    low = fields.Float(string='Low Threshold')
    high = fields.Float(string='High Threshold')
    format = fields.Char(string='Format')
    decimals = fields.Integer(string='Decimals')


class SalesKPICalc(models.Model):
    _name = 'sales.kpi.calc'
    _description = 'Sales KPI Calculation Data'

    kpi_id = fields.Many2one('sales.kpi', string='Related KPI', required=True)
    calc_name = fields.Char(string='Calculation Name')
    goal = fields.Float(string='Monthly Goal')
    number = fields.Integer(string='Calculation Number')
    other_calculations = fields.Float(string='Other Calculation Fields')


class SalesKPIDashboard(models.Model):
    _name = 'sales.kpi.dashboard'
    _description = 'Sales KPI Dashboard Data'

    kpi_id = fields.Many2one('sales.kpi', string='Related KPI', required=True)
    dashboard_metric = fields.Char(string='Dashboard Metric')
    value = fields.Float(string='Value')
    summary = fields.Text(string='Summary')
    other_dashboard_fields = fields.Char(string='Additional Dashboard Fields')
