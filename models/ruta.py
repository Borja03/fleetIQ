from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Ruta(models.Model):
    _name = "fleetiq.ruta"
    _description = "Rutas de los vehículos"

    localizador = fields.Char(string="Localizador", compute="_compute_localizador", store=True, readonly=True)
    name = fields.Char(string="Nombre de la Ruta", required=True)
    origen = fields.Char(string="Origen", required=True)
    destino = fields.Char(string="Destino", required=True)
    distancia = fields.Float(string="Distancia (km)", required=True)
    tiempo = fields.Float(string="Tiempo Estimado (horas)", required=True)
    fecha_creacion = fields.Date(string="Fecha de Creación", default=fields.Date.today)

    vehicles = fields.Many2many(
        comodel_name="fleetiq.vehiculo",
        relation="fleetIQ_vehiculo",
        column1="ruta_id",
        column2="matricula",
        string="Vehículos"
    )

    @api.depends('origen', 'destino')
    def _compute_localizador(self):
        for record in self:
            if record.origen and record.destino:
                record.localizador = (record.origen[:3] + record.destino[:3]).upper()
            else:
                record.localizador = ''

    @api.onchange('origen', 'destino')
    def _onchange_generate_localizador(self):
        if self.origen and self.destino:
            self.localizador = (self.origen[:3] + self.destino[:3]).upper()

    @api.constrains('distancia', 'tiempo', 'origen', 'destino')
    def _check_valid_data(self):
        for record in self:
            if record.distancia <= 0:
                raise ValidationError("La distancia debe ser un valor positivo.")
            if record.tiempo <= 0:
                raise ValidationError("El tiempo estimado debe ser un valor positivo.")
            if record.origen == record.destino:
                raise ValidationError("El origen y el destino no pueden ser iguales.")

    @api.model
    def create(self, vals):
        if 'origen' in vals and 'destino' in vals:
            vals['localizador'] = (vals['origen'][:3] +'-'+ vals['destino'][:3]).upper()
        return super(Ruta, self).create(vals)
