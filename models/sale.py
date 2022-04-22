# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class SalesOrder(models.Model):
    _inherit = "sale.order"

    sale_description = fields.Text(string='Sale Description')

    approval_state = fields.Selection([
        ('draft', 'Draft'),
        ('waiting_sales_manager_approval', 'Waiting Sales Manager Approval'),
        ('waiting_advisor_approval', 'Waiting Advisor Approval'),
        ('approved', 'Approved'),
        ('disapproved', 'Disapproved'),
    ], compute='_compute_state',
        default='draft', string="Approval State",
        required=True,
    )

    @api.depends('order_line.approval_state')
    def _compute_state(self):
        for rec in self:
            for line in rec.order_line:
                if line.approval_state == 'disapproved':
                    rec.approval_state = 'disapproved'
                    break
                elif line.approval_state == 'waiting_sales_manager_approval':
                    rec.approval_state = 'waiting_sales_manager_approval'
                    break
                elif line.approval_state == 'waiting_advisor_approval':
                    rec.approval_state = 'waiting_advisor_approval'
                    break
                else:
                    rec.approval_state = "approved"

    def action_confirm(self):
        for rec in self:
            if rec.approval_state != 'approved':
                raise ValidationError(_("Sorry, You can not confirm that hasn't a DONE status!"))
        return super(SalesOrder, self).action_confirm()


class SalesOrderLine(models.Model):
    _inherit = "sale.order.line"

    approval_state = fields.Selection([
        ('waiting_sales_manager_approval', 'Waiting Sales Manager Approval'),
        ('waiting_advisor_approval', 'Waiting Advisor Approval'),
        ('approved', 'Approved'),
        ('disapproved', 'Disapproved'),
    ], compute='_compute_state',
        default='approved', string="State",
        required=True,
        store=True,
    )

    @api.depends('discount')
    def _compute_state(self):
        for rec in self:
            if rec.product_id.sales_person_max_discount:
                if rec.product_id.sales_person_max_discount < int(rec.discount):
                    rec.approval_state = "waiting_sales_manager_approval"
                else:
                    rec.approval_state = "approved"
            else:
                if rec.product_id.categ_id.sales_person_max_discount < int(rec.discount):
                    rec.approval_state = "waiting_sales_manager_approval"
                else:
                    rec.approval_state = "approved"

    def action_approve_manager(self):
        for rec in self:
            if rec.product_id.sales_manager_max_discount:
                if rec.product_id.sales_manager_max_discount < int(rec.discount):
                    print(rec.approval_state)
                    rec.approval_state = 'waiting_advisor_approval'
                else:
                    rec.approval_state = "approved"
            else:
                if rec.product_id.categ_id.sales_manager_max_discount < int(rec.discount):
                    print(rec.approval_state)
                    rec.approval_state = 'waiting_advisor_approval'
                else:
                    rec.approval_state = "approved"

    def action_approve_advisor(self):
        for rec in self:
            rec.approval_state = 'approved'

    def action_disapprove(self):
        for rec in self:
            if rec.approval_state != 'disapproved':
                rec.approval_state = 'disapproved'
            else:
                raise ValidationError(_("Sorry, has already disapproved state!"))
