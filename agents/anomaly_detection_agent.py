class AnomalyDetectionAgent:
    def handle(self, network_result):
        metrics = network_result["metrics"]

        anomaly_detected = (
            metrics["latency_ms"] > 100
            or metrics["packet_loss"] > 3
            or metrics["tower_load"] > 85
            or metrics["signal_strength"] < 50
        )

        if anomaly_detected:
            response = (
                "Anomaly detected. The issue may be caused by high tower load, weak signal, "
                "packet loss, or abnormal latency."
            )
            confidence = 0.9
        else:
            response = "No major network anomaly detected. Your current network metrics look stable."
            confidence = 0.87

        return {
            "agent": "Anomaly Detection Agent",
            "response": response,
            "confidence": confidence,
            "anomaly_detected": anomaly_detected,
            "metrics": metrics
        }
