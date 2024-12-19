from odoo import fields, models

class Vehiculo(models.Model):
    _name = "fleetiq.vehiculo"
    _description = "Vehículos"

    vehiculo_id = fields.Integer(string="ID")
    fecha_itv = fields.Datetime(string="Fecha de ITV")
    fecha_matriculacion = fields.Datetime(string="Fecha de Matriculación")
    matricula = fields.Char(string="Matrícula", required=True)
    active = fields.Boolean(string="Activo", default=True)
    capacidad = fields.Integer(string="Capacidad del Vehículo")
    modelo = fields.Char(string="Modelo")

    # Relación Many2one con el envío
    envio_id = fields.Many2one('fleetiq.envio', string="Envío")

    # Relación One2many con RutaVehiculo
    asignaciones_ruta = fields.One2many(
        'fleetiq.rutavehiculo',  # Comodel
        'vehiculo_id',          # Campo en RutaVehiculo que referencia Vehiculo
        string="Asignaciones de Rutas"
    )
