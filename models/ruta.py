from odoo import fields, models


class Ruta(models.Model):
    _name = "fleetiq.ruta"
    _description = "Rutas de los vehículos"


    localizador = fields.Char(string="Localizador", required=True)
    name = fields.Char(string="Nombre de la Ruta", required=True)
    origen = fields.Char(string="Origen", required=True)
    destino = fields.Char(string="Destino", required=True)
    distancia = fields.Float(string="Distancia (km)", required=True)
    tiempo = fields.Float(string="Tiempo Estimado (horas)", required=True)
    fecha_creacion = fields.Date(string="Fecha de Creación", default=fields.Date.today)

    # Campo para ver las matrículas de los vehículos relacionados
    vehicles = fields.Many2many(
        comodel_name="fleetiq.vehiculo",
        relation="fleetIQ_rutavehiculo",
        column1="ruta_id",
        column2="vehiculo_matricula",
        string="Vehículos"
    )
