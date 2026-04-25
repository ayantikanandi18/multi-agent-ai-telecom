class BillingAgent:
    def handle(self, context):
        query = context["query"].lower()

        if "refund" in query:
            response = (
                "I found this as a refund-related billing issue. Please verify the payment date, "
                "transaction ID, and whether the charge came from plan fees, roaming, device installment, or add-ons."
            )

        elif "charge" in query:
            response = (
                "This looks like an unexpected charge issue. Common causes include taxes, late fees, "
                "international roaming, device installments, or premium add-ons."
            )

        elif "payment" in query:
            response = (
                "For one-time payment, confirm your phone number, ZIP code, payment method, "
                "and account balance before submitting the payment."
            )

        else:
            response = (
                "I can help review your bill, explain charges, verify payments, or start a refund workflow."
            )

        return {
            "agent": "Billing Intelligence Agent",
            "response": response,
            "confidence": 0.92
        }
