from utils.mock_data import get_network_metrics

class NetworkMonitoringAgent:
    def handle(self, context):
        metrics = get_network_metrics(context["region"])

        response = (
            f"Network check completed for {context['region']}. "
            f"Latency: {metrics['latency_ms']}ms, "
            f"Packet Loss: {metrics['packet_loss']}%, "
            f"Signal Strength: {metrics['signal_strength']}%, "
            f"Tower Load: {metrics['tower_load']}%."
        )

        return {
            "agent": "Network Monitoring Agent",
            "response": response,
            "confidence": 0.88,
            "metrics": metrics
        }
