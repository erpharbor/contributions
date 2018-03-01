odoo.define('hr_web_camera.web_camera', function (require) {
"use strict";

var core = require('web.core');
var ajax = require('web.ajax');
var FormView = require('web.FormView');

//var _t = core._t;
//var _lt = core._lt;
var QWeb = core.qweb;

FormView.include({
    render_buttons: function($node) {
        this._super($node)
        var self = this;
        if (this.dataset.model == "wiz.capture.pic") {
            Webcam.set({
                width: 320,
                height: 240,
                image_format: 'jpeg',
                jpeg_quality: 90
            });
            $(QWeb.render("hr_web_camera")).appendTo(this.$buttons)
            this.$buttons.find('.o_form_button_start_camera').click(function() {
                var emp_id = self.dataset.context.active_ids[0]
                var datas = {
                    'file_data': $('#img_result').val(),
                    'employee_id': emp_id,
                }
                $.ajax({
                    url: '/hr_web_camera/capture',
                    dataType: 'json',
                    type: 'POST',
                    data: datas,
                    success: function (html) {
                        $.unblockUI();
                        alert('Image captured successfully.');
                        location.reload();
                    },
                    error: function (html) {
                        $.unblockUI();
                        alert('Something went wrong. Please try again.')
                    }
                })
            });
        }
    },
})

});
