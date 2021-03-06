import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Addon(Model):

    fields = ["id", "name", "invoice_name", "description", "type", "charge_type", "price", \
    "currency_code", "period", "period_unit", "unit", "status", "archived_at", "enabled_in_portal", \
    "tax_code", "sku", "accounting_code", "accounting_category1", "accounting_category2", "resource_version", \
    "updated_at", "invoice_notes", "taxable", "tax_profile_id", "meta_data"]


    @staticmethod
    def create(params, env=None, headers=None):
        return request.send('post', request.uri_path("addons"), params, env, headers)

    @staticmethod
    def update(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("addons",id), params, env, headers)

    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("addons"), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("addons",id), None, env, headers)

    @staticmethod
    def delete(id, env=None, headers=None):
        return request.send('post', request.uri_path("addons",id,"delete"), None, env, headers)

    @staticmethod
    def copy(params, env=None, headers=None):
        return request.send('post', request.uri_path("addons","copy"), params, env, headers)

    @staticmethod
    def unarchive(id, env=None, headers=None):
        return request.send('post', request.uri_path("addons",id,"unarchive"), None, env, headers)
