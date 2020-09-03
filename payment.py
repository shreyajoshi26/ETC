from odoo import models, fields, api


class payment(models.Model):
    _name = "payment"
    _rec_name = 'user_id'
    user_id = fields.Many2one('res.users', string="User")
    branch_id = fields.Integer(string="Branch_Id")
    contact_no = fields.Integer(string="Contact No")


class tollauthority(models.Model):
    _name = "toll.authority"
    _rec_name = 'user_id'
    user_id = fields.Many2one('res.users', string="User")
    toll_amount = fields.Float(string="tollamount")
    rfid_no = fields.Char(string="rfidno")


class tolllocation(models.Model):
    _name = "toll.location"
    _rec_name = 'location_1'
    location_1 = fields.Char(string="location1")
    location_2 = fields.Char(string="location2")


class tollinformation(models.Model):
    _name = "toll.information"
    _rec_name = 'location_id'

    location_id = fields.Many2one('toll.location', string="Location")
    toll_ids = fields.One2many('toll.amount', 'info_id')

class toll_amount(models.Model):
    _name = 'toll.amount'

    info_id = fields.Many2one('toll.information')
    name = fields.Selection(
        [('C/J/V', 'Car/Jeep/Van'), ('LCV', 'light commercial vehicle'), ('bus/truck', 'bus/truck'),
         ('EM/HCM', 'Earth moving/heavy construction machinary'), ('TRCT', 'tractor'),
         ('MLCV', 'mini light commercial vehicle')], required=True)
    type = fields.Selection([('one_way', 'One Way'), ('two_way', 'Two Way')], required=True)
    currency_id = fields.Many2one('res.currency', string='Currency', required=True,
                                  default=lambda self: self.env.user.company_id.currency_id)
    amount = fields.Monetary(currency_field='currency_id',string="Amount", required=True)

class resuser(models.Model):
    _inherit = 'res.users'
    rfid_no = fields.Char(string="RFID",required="true")
    vehicle_no = fields.Char(string="Vehicle No.",required="true")
    vehicle_type = fields.Selection(
        [('C/J/V', 'Car/Jeep/Van'), ('LCV', 'light commercial vehicle'),('bus/truck', 'bus/truck'),
         ('EM/HCM','Earth moving/heavy construction machinary'),('TRCT','tractor'),('MLCV','mini light commercial vehicle')], string="Vehicle Type")

class feedback(models.Model):
    _name='toll.feedback'
    user_id = fields.Many2one('res.users', string="User")
    feedback=fields.Text(string='feedback')


class WebsiteConfig(models.TransientModel):

    _inherit = 'website.config.settings'

    raspi_ip = fields.Char('Raspi IP Address')

    @api.model
    def default_get(self, fields):
        obj = self.search([])
        res = super(WebsiteConfig, self).default_get(fields)
        if obj:
            dc = obj.read()[0]
            del dc["write_uid"], dc["id"], dc["__last_update"], dc["create_date"]
            res.update(dc)
        return res

    @api.model
    def create(self, vals):
        obj = self.search([])
        if not obj:
            return super(WebsiteConfig, self).create(vals)
        obj[0].write(vals)
        return obj[0]