from odoo import api, fields, models, _
from datetime import date
import logging

_logger = logging.getLogger(__name__)
class CheckInvoices(models.Model):
    _name = 'account.invoice'
    _inherit = 'account.invoice'

    @api.model
    def _cron_check_invoice(self):
        today = date.today()
        invoices = self.env['account.invoice'].search([
            ('date_due', '<=', today),
            ('state', '=', 'open')
        ])

        for invoice in invoices:
            partner = invoice.partner_id
            partner.sale_warn = 'block'
        