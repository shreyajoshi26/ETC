from odoo import http, _
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request
from odoo.addons.web.controllers.main import ensure_db, Home
from odoo.addons.auth_signup.models.res_users import SignupError
import logging

_logger = logging.getLogger(__name__)

class WebsiteSale(WebsiteSale):

    @http.route(['/page/homepage'], type='http', auth='public', website=True)
    def home_page_view(self,**post):
        prod_categ_id = request.env['product.public.category'].sudo().search([('name','=ilike','our products')], limit=1).id
        products = request.env['product.template'].sudo().search([('public_categ_ids', 'in', prod_categ_id)])
        return request.render('Rozgaar.custom_home_page', {'products': products})

    @http.route(['/products'], type='http', auth="public", website=True)
    def product1_page(self, **post):
        return request.render('Rozgaar.product_page',{})

    @http.route(['/snacks'], type='http', auth="public", website=True)
    def snacks_page(self, **post):
        return request.render('Rozgaar.snacks_page', {})

    @http.route(['/decorations'], type='http', auth="public", website=True)
    def decoration_page(self, **post):

        return request.render('Rozgaar.decoration_page', {})

    @http.route(['/clay_models'], type='http', auth="public", website=True)
    def claymodel_page(self, **post):
        return request.render('Rozgaar.claymodel_page', {})

    @http.route(['/demand'], type='http', auth="public", website=True)
    def demand_page(self, **post):
        return request.render('Rozgaar.demand_page', {})

    @http.route(['/supply'], type='http', auth="public", website=True)
    def supply_page(self, **post):
        return request.render('Rozgaar.supply_page', {})

    @http.route(['/register'], type='http', auth="public", website=True)
    def register_page(self, **post):
        if post:
            request.env['user.information'].sudo().create({
                'name': post.get('name'),
                'category':post.get('category'),
                'user_id': post.get('user_id'),
                'address': post.get('address'),
                'contact_no': post.get('contact_no'),
                'password': post.get('password'),
            })
            return request.redirect('/page/homepage')
        return request.render('Rozgaar.register')

    @http.route(['/add_to_cart'],type='http',csrf=False,method=['post'],auth="public",website=True)
    def add_to_order_page(self,**post):
        if post and post.get('product_id'):
            p_id=request.env['product.template'].search([('id','=',post.get('product_id'))])
            request.website.sale_get_order(force_create=1)._cart_update( product_id=int(p_id),
                add_qty=float(1),
                attributes=self._filter_attributes(**post),)
            return request.redirect("/shop/cart")


class AuthSignupHome(Home):

    @http.route('/web/signup', type='http', auth='public', website=True)
    def web_auth_signup(self, *args, **kw):
        print ("")
        qcontext = self.get_auth_signup_qcontext()

        if not qcontext.get('token') and not qcontext.get('signup_enabled'):
            raise werkzeug.exceptions.NotFound()

        if 'error' not in qcontext and request.httprequest.method == 'POST':
            try:
                self.do_signup(qcontext)
                return super(AuthSignupHome, self).web_login(*args, **kw)
            except (SignupError, AssertionError), e:
                if request.env["res.users"].sudo().search([("login", "=", qcontext.get("login"))]):
                    qcontext["error"] = _("Another user is already registered using this email address.")
                else:
                    _logger.error(e.message)
                    qcontext['error'] = _("Could not create a new account.")

        return request.render('auth_signup.signup', qcontext)

    def do_signup(self, qcontext):
        """ Shared helper that creates a res.partner out of a token """
        values = { key: qcontext.get(key) for key in ('login', 'name', 'password', 'category') }
        assert values.values(), "The form was not properly filled in."
        assert values.get('password') == qcontext.get('confirm_password'), "Passwords do not match; please retype them."
        supported_langs = [lang['code'] for lang in request.env['res.lang'].sudo().search_read([], ['code'])]
        if request.lang in supported_langs:
            values['lang'] = request.lang
        self._signup_with_values(qcontext.get('token'), values)
        request.env.cr.commit()