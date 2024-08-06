# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, tools, _


class BaseModel(models.AbstractModel):
    _inherit = 'base'

    # override master create function
    @api.model_create_multi
    def create(self, vals_list):
        
	# Add Your custom here .

        return super(BaseModel, self).create(vals_list)
