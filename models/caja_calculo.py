from odoo import models, fields, api

class CajaCalculo(models.Model):
    _name = 'caja.calculo'
    _description = 'Cálculo de Caja'

    name = fields.Char(string='Descripción', required=True)
    entrada_actual = fields.Float(string='Entrada Actual')
    entrada_anterior = fields.Float(string='Entrada Anterior')
    salida_actual = fields.Float(string='Salida Actual')
    salida_anterior = fields.Float(string='Salida Anterior')
    ent_act_menos_ant = fields.Float(string='Entrada Actual - Anterior', compute='_compute_calculo', store=True)
    sal_act_menos_ant = fields.Float(string='Salida Actual - Anterior', compute='_compute_calculo', store=True)
    entrada_menos_salida = fields.Float(string='Entrada - Salida', compute='_compute_calculo', store=True)
    resultadox100 = fields.Float(string='Resultado x 100', compute='_compute_calculo', store=True)
    
    @api.depends('entrada_actual', 'entrada_anterior', 'salida_actual', 'salida_anterior')
    def _compute_calculo(self):
        for record in self:
            record.ent_act_menos_ant = record.entrada_actual - record.entrada_anterior
            record.sal_act_menos_ant = record.salida_actual - record.salida_anterior
            record.entrada_menos_salida = record.ent_act_menos_ant - record.sal_act_menos_ant
            record.resultadox100 = record.entrada_menos_salida * 100
