# -*- coding: utf-8 -*-
from odoo import fields, models, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # -- Field Declarations --
    is_customer = fields.Boolean(
        string="Is a Customer",
        compute='_compute_contact_roles',
        inverse='_inverse_is_customer',
        help="Check this box if this contact is a customer."
    )
    is_vendor = fields.Boolean(
        string="Is a Vendor",
        compute='_compute_contact_roles',
        inverse='_inverse_is_vendor',
        help="Check this box if this contact is a vendor/supplier."
    )

    # -- Compute Method --
    @api.depends('customer_rank', 'supplier_rank')
    def _compute_contact_roles(self):
        """
        Sets the boolean fields based on the rank values.
        A partner is considered a customer/vendor if their rank is greater than 0.
        """
        for partner in self:
            partner.is_customer = partner.customer_rank > 0
            partner.is_vendor = partner.supplier_rank > 0

    # -- Inverse Methods --
    def _inverse_is_customer(self):
        """
        When the 'is_customer' checkbox is changed, this method updates the
        customer_rank to reflect the new state.
        """
        for partner in self:
            if partner.is_customer and partner.customer_rank == 0:
                # If checked and rank is 0, set rank to 1
                partner.customer_rank = 1
            elif not partner.is_customer and partner.customer_rank > 0:
                # If unchecked, set rank to 0. A simple approach is taken here.
                partner.customer_rank = 0

    def _inverse_is_vendor(self):
        """
        When the 'is_vendor' checkbox is changed, this method updates the
        supplier_rank to reflect the new state.
        """
        for partner in self:
            if partner.is_vendor and partner.supplier_rank == 0:
                # If checked and rank is 0, set rank to 1
                partner.supplier_rank = 1
            elif not partner.is_vendor and partner.supplier_rank > 0:
                # If unchecked, set rank to 0
                partner.supplier_rank = 0