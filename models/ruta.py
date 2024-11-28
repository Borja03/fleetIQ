from odoo import fields, models

class Ruta(models.Model):
    _name = "FleetIQ.ruta"
    _description = "Rutas de los vehiculos"

    name = fields.Char(string="Nombre de la Ruta", required=True)
    distancia = fields.Float(string="Distancia (km)", required=True)
    tiempo_estimado = fields.Float(string="Tiempo Estimado (horas)", required=True)
    fecha_creacion = fields.Date(string="Fecha de Creación", default=fields.Date.today)
    estado = fields.Selection(
        [
            ('nueva', 'Nueva'),
            ('en_proceso', 'En Proceso'),
            ('completada', 'Completada'),
        ],
        string="Estado",
        default="nueva",
    )
    # Relación con RutaVehiculo
    ruta_vehiculo_ids = fields.One2many(
        'FleetIQ.rutavehiculo', 'ruta_id', string="Vehículos Asignados"
    )

