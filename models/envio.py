from odoo import models, fields

class Envio(models.Model):
    _name = "fleetiq.envio"

    envio_id = fields.Integer(string="ID")
    fecha_envio = fields.Datetime(string="Fecha de Envio")
    fecha_entrega = fields.Datetime(string="Fecha de Entrega")
    num_paquetes = fields.Integer(string="Número de Paquetes")
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_transito', 'En Transito'),
        ('entregado', 'Entregado')
    ], string="Estado del Envío")

    # Relación Many2one con el vehículo
    vehiculo_id = fields.Many2one('fleetiq.vehiculo', string="Vehículo")

    # Relacionar con la matrícula del vehículo, usando el campo related
    vehiculo_matricula = fields.Char(
        string="Matrícula del Vehículo",
        related="vehiculo_id.matricula",  # Aquí accedemos correctamente al campo 'matricula' del vehículo
        store=True
    )

    # Campo calculado para la ruta
    ruta_id = fields.Char(
        string="Ruta",
        compute="_compute_ruta",
        store=True
    )

    def _compute_ruta(self):
        for record in self:
            if record.ruta_id:
                ruta = self.env['fleetiq.ruta'].search([
                    ('id', '=', record.ruta_id)
                ], limit=1)
                if ruta:
                    origen_code = ruta.origen[:3] if ruta.origen else ''
                    destino_code = ruta.destino[:3] if ruta.destino else ''
                    record.ruta_id = f"{origen_code}-{destino_code}"
                else:
                    record.ruta_id = ''
            else:
                record.ruta_id = ''
