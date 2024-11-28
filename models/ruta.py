from odoo import fields, models


class Ruta(models.Model):
    _name = "FleetIQ.ruta"
    _description = "Rutas de los vehiculos"

    # Campos básicos
    name = fields.Char(string="Nombre de la Ruta", required=True)
    origen = fields.Char(string="Origen", required=True)
    destino = fields.Char(string="Destino", required=True)
    distancia = fields.Float(string="Distancia (km)", required=True)
    tiempo = fields.Float(string="Tiempo Estimado (horas)", required=True)
    localizador = fields.Char(string="Localizador", required=True)
    fecha_creacion = fields.Date(string="Fecha de Creación", default=fields.Date.today)

    # Campo de estado
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
        'FleetIQ.rutaVehiculo', 'ruta_id', string="Vehículos Asignados"
    )


