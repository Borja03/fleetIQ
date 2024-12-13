from odoo import models, fields

class FleetiqUser(models.Model):
    _name = 'fleetiq.user'
    _description = 'Base User Model'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one(
        'res.partner',
        required=True,
        ondelete='cascade'
    )

    user_category = fields.Selection([
        ('admin', 'Admin'),
        ('trabajador', 'Trabajador')
    ], string='User Category', required=True, default='trabajador')

    password_hash = fields.Char(string='Password Hash')

    # Disable conflicting field
    channel_ids = False


class FleetiqAdmin(models.Model):
    _name = 'fleetiq.admin'
    _description = 'Admin User'
    _inherit = 'fleetiq.user'

    fleetiq_user_id = fields.Many2one(
        'fleetiq.user',
        string='Related User',
        required=True,
        ondelete='cascade'
    )

    last_login = fields.Datetime(string='Last Login')


class FleetiqTrabajador(models.Model):
    _name = 'fleetiq.trabajador'
    _description = 'Worker User'
    _inherit = 'fleetiq.user'

    fleetiq_user_id = fields.Many2one(
        'fleetiq.user',
        string='Related User',
        required=True,
        ondelete='cascade'
    )

    department = fields.Char(string='Department')