# -*- coding: utf-8 -*-
import requests
from odoo import models

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def button_confirm(self):
        # Call original logic first
        res = super(PurchaseOrder, self).button_confirm()

        # Send API request for each PO
        for po in self:
            try:
                payload = {
                    'po_number': po.name,
                    'vendor': po.partner_id.name,
                    'order_date': str(po.date_order),
                    'lines': [{
                        'product': line.product_id.name,
                        'qty': line.product_qty,
                        'price': line.price_unit,
                    } for line in po.order_line]
                }

                # Replace this URL with your actual API endpoint
                api_url = "https://your-api-endpoint.com/receive_po"

                response = requests.post(api_url, json=payload, timeout=10)

                response.raise_for_status()
            except Exception as e:
                # Log error in Odoo log
                po.message_post(
                    body=f"API call failed: {str(e)}"
                )

        return res
