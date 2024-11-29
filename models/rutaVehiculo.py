from odoo import fields, models
class RutaVehiculo(models.Model):
    _name = "fleetIQ.rutavehiculo"
    _description = "Asignación de Vehículos a Rutas"

    fecha_asignacion = fields.Date(string="Fecha de Asignación", required=True, default=fields.Date.today)
    ruta_id = fields.Many2one(
        'FleetIQ.ruta', string="Ruta", required=True, ondelete="cascade"
    )

    envio_id = fields.Many2one(
        'FleetIQ.envio', string="Envio", required=True, ondelete="cascade"
    )

    vehiculo_id = fields.Many2one(
        'FleetIQ.vehiculo', string="Vehiculo", required=True, ondelete="cascade"
    )
