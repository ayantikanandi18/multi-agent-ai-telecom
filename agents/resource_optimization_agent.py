class ResourceOptimizationAgent:
    def handle(self, anomaly_result):
        metrics = anomaly_result["metrics"]

        recommendations = []

        if metrics["tower_load"] > 85:
            recommendations.append("reroute traffic to a nearby tower")

        if metrics["latency_ms"] > 100:
            recommendations.append("prioritize low-latency network path")

        if metrics["packet_loss"] > 3:
            recommendations.append("trigger packet-loss mitigation workflow")

        if metrics["signal_strength"] < 50:
            recommendations.append("recommend manual network reset or tower handoff")

        response = "Recommended optimization actions: " + ", ".join(recommendations) + "."

        return {
            "agent": "Resource Optimization Agent",
            "response": response,
            "confidence": 0.91
        }
