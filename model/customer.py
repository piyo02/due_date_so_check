from odoo import api, fields, models, _
import logging

_logger = logging.getLogger(__name__)
class DueDateCustomer(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    due_date_customer = fields.Integer('due date', default=60)