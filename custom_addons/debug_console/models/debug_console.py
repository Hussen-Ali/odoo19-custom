from odoo import models, fields
import logging

_logger = logging.getLogger(__name__)


class DebugConsole(models.Model):
    _name = "debug.console"
    _description = "Debug Console Tool"

    output = fields.Text(string="Output")

    def action_run_test(self):
        lines = []

        currencies = self.env["res.currency"].search([])

        lines.append("=== CURRENCIES ===")
        for c in currencies:
            msg = f"{c.name} | rate={c.rate}"
            lines.append(msg)
            _logger.info(msg)

        usd = self.env["res.currency"].search([("name", "=", "USD")], limit=1)
        company = self.env.company.currency_id

        lines.append("\n=== CONVERSION ===")
        lines.append(f"Company: {company.name}")

        if usd:
            lines.append(f"USD rate: {usd.rate}")
            conv = company.rate / usd.rate if usd.rate else 0
            lines.append(f"1 USD = {conv} {company.name}")
            _logger.info("Conversion: %s", conv)
        else:
            lines.append("USD not found")

        self.output = "\n".join(lines)

        return {
            "type": "ir.actions.client",
            "tag": "reload",
        }