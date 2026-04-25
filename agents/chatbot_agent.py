class ChatbotAgent:
    def detect_intent(self, query):
        query = query.lower()

        if any(word in query for word in ["bill", "payment", "invoice", "charge", "refund"]):
            return "billing"

        if any(word in query for word in ["network", "signal", "slow", "internet", "5g", "latency", "no service"]):
            return "network"

        if any(word in query for word in ["human", "ticket", "complaint", "escalate"]):
            return "escalation"

        return "general"
