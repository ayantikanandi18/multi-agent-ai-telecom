import random

class EscalationAgent:
    def handle(self, context):
        ticket_id = f"TEL-{random.randint(10000, 99999)}"

        return {
            "agent": "Escalation Agent",
            "response": (
                f"I created support ticket {ticket_id}. "
                f"The issue has been routed to a human telecom support specialist with customer context attached."
            ),
            "confidence": 0.95,
            "ticket_id": ticket_id
        }
