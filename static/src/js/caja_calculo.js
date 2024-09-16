odoo.define('caja_calculo.FormController', function (require) {
"use strict";

var FormController = require('web.FormController');

var CajaCalculoFormController = FormController.extend({
    _onFieldChanged: function (event) {
        this._super.apply(this, arguments);
        var fieldName = event.name;
        if (['entrada_actual', 'entrada_anterior', 'salida_actual', 'salida_anterior'].includes(fieldName)) {
            this.trigger_up('field_changed', {
                dataPointID: this.handle,
                changes: {},
                viewType: 'form',
            });
        }
    },
});

return CajaCalculoFormController;

});
