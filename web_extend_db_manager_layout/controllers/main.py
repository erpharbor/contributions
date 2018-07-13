# -*- coding: utf-8 -*-
import jinja2
import json

import odoo
from odoo import http
from odoo.addons.web.controllers.main import DBNAME_PATTERN, db_monodb,\
    Database as DB

loader = jinja2.PackageLoader('odoo.addons.web_extend_db_manager_layout',
                              "views")
env = jinja2.Environment(loader=loader, autoescape=True)
env.filters["json"] = json.dumps


class Database(DB):

    def _render_template(self, **d):
        d.setdefault('manage', True)
        d['insecure'] = odoo.tools.config['admin_passwd'] == 'admin'
        d['list_db'] = odoo.tools.config['list_db']
        d['langs'] = odoo.service.db.exp_list_lang()
        d['countries'] = odoo.service.db.exp_list_countries()
        d['pattern'] = DBNAME_PATTERN
        # databases list
        d['databases'] = []
        try:
            d['databases'] = http.db_list()
        except odoo.exceptions.AccessDenied:
            monodb = db_monodb()
            if monodb:
                d['databases'] = [monodb]
        return env.get_template("database_manager.html").render(d)
