from odoo import api, fields, models, _
from datetime import date, timedelta
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
            
            due_date_customer = partner.due_date_customer
            due_date = invoice.date_due + timedelta(days=due_date_customer)

            if due_date < today:
                partner.sale_warn = 'block'
                partner.sale_warn_msg = 'Ada tagihan jatuh tempo'
        