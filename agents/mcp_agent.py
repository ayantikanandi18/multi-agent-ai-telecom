class MCPAgent:
    def __init__(self):
        self.memory = []

    def get_context(self, query, intent):
        return {
            "query": query,
            "intent": intent,
            "customer_id": "CUST-1029",
            "plan": "Unlimited 5G",
            "region": "New York",
            "device": "iPhone 15",
            "memory": self.memory[-5:]
        }

    def update_memory(self, query, intent, result):
        self.memory.append({
            "query": query,
            "intent": intent,
            "response": result["response"]
        })
