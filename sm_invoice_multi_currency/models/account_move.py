# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    company_amount_untaxed = fields.Monetary(
        string='Untaxed Amount (Company)',
        compute='_compute_company_amounts',
        currency_field='company_currency_id',
        store=True,
    )
    company_amount_tax = fields.Monetary(
        string='Tax (Company)',
        compute='_compute_company_amounts',
        currency_field='company_currency_id',
        store=True,
    )
    company_amount_total = fields.Monetary(
        string='Total (Company)',
        compute='_compute_company_amounts',
        currency_field='company_currency_id',
        store=True,
    )
    company_amount_residual = fields.Monetary(
        string='Amount Due (Company)',
        compute='_compute_company_amounts',
        currency_field='company_currency_id',
        store=True,
    )

    @api.depends('amount_untaxed', 'amount_tax', 'amount_total', 'amount_residual', 'currency_id', 'company_currency_id', 'invoice_date', 'date')
    def _compute_company_amounts(self):
        for move in self:
            date = move.invoice_date or move.date or fields.Date.context_today(self)
            currency = move.currency_id
            company_currency = move.company_currency_id
            company = move.company_id or self.env.company
            
            # Convert values from currency_id to company_currency_id
            move.company_amount_untaxed = currency._convert(move.amount_untaxed, company_currency, company, date)
            move.company_amount_tax = currency._convert(move.amount_tax, company_currency, company, date)
            move.company_amount_total = currency._convert(move.amount_total, company_currency, company, date)
            move.company_amount_residual = currency._convert(move.amount_residual, company_currency, company, date)
