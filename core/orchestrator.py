from agents.chatbot_agent import ChatbotAgent
from agents.mcp_agent import MCPAgent
from agents.billing_agent import BillingAgent
from agents.network_monitoring_agent import NetworkMonitoringAgent
from agents.anomaly_detection_agent import AnomalyDetectionAgent
from agents.resource_optimization_agent import ResourceOptimizationAgent
from agents.escalation_agent import EscalationAgent


class TelecomOrchestrator:
    def __init__(self):
        self.chatbot_agent = ChatbotAgent()
        self.mcp_agent = MCPAgent()
        self.billing_agent = BillingAgent()
        self.network_agent = NetworkMonitoringAgent()
        self.anomaly_agent = AnomalyDetectionAgent()
        self.optimization_agent = ResourceOptimizationAgent()
        self.escalation_agent = EscalationAgent()

    def handle_user_query(self, user_query):
        intent = self.chatbot_agent.detect_intent(user_query)

        context = self.mcp_agent.get_context(user_query, intent)

        if intent == "billing":
            result = self.billing_agent.handle(context)

        elif intent == "network":
            network_status = self.network_agent.handle(context)
            anomaly_result = self.anomaly_agent.handle(network_status)

            if anomaly_result["anomaly_detected"]:
                result = self.optimization_agent.handle(anomaly_result)
            else:
                result = network_status

        elif intent == "escalation":
            result = self.escalation_agent.handle(context)

        else:
            result = {
                "response": (
                    "I can help with billing, network issues, SIM/eSIM, roaming, "
                    "plan support, or ticket escalation. Please share more details."
                ),
                "confidence": 0.65
            }

        if result["confidence"] < 0.7:
            result = self.escalation_agent.handle(context)

        self.mcp_agent.update_memory(user_query, intent, result)

        return {
            "final_response": result["response"],
            "intent": intent,
            "agent_used": result.get("agent", "Chatbot Agent"),
            "confidence": result["confidence"]
        }
