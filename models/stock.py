from odoo import api, fields, models


class ReturnPicking(models.TransientModel):
    _inherit = 'stock.return.picking'



    # @api.model
    # def default_get(self, fields):
    #     print 'default_get'
    #     res = super(ReturnPicking, self).default_get(fields)
    #     picking = self.env['stock.picking'].browse(self.env.context.get('active_id'))
    #     if picking:
    #         code = picking.picking_type_id and picking.picking_type_id.code or ''
    #         res.update({'operation_type': code})
    #     return res

    # @api.model
    # def default_get(self, fields):
    #     print 'default_get'
    #     res = super(ReturnPicking, self).default_get(fields)
    #     picking = self.env['stock.picking'].browse(self.env.context.get('active_id'))
    #     if picking:
    #         has_partner = False
    #         if picking.partner_id:
    #             has_partner = True
    #             res.update({'has_partner': has_partner})
    #     return res

    #operation_type = fields.Char()
    #has_partner = fields.Boolean()
    location_id = fields.Many2one(
        'stock.location', 'Return Location',
        domain="[(1 ,'=', 1)]"
       )


    # location_id = fields.Many2one(
    #     'stock.location', 'Return Location',
    #     domain="['|', ('id', '=', original_location_id), '&', ('return_location', '=', True), ('id', 'child_of', parent_location_id)]")
