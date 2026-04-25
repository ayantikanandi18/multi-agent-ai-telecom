from core.orchestrator import TelecomOrchestrator

def main():
    orchestrator = TelecomOrchestrator()

    print("\n🚀 Telecom Multi-Agent AI System")
    print("Type 'exit' to quit.\n")

    while True:
        user_query = input("User: ")

        if user_query.lower() == "exit":
            print("Assistant: Goodbye!")
            break

        response = orchestrator.handle_user_query(user_query)
        print(f"\nAssistant: {response['final_response']}")
        print(f"Intent: {response['intent']}")
        print(f"Agent Used: {response['agent_used']}")
        print(f"Confidence: {response['confidence']}")
        print("-" * 60)

if __name__ == "__main__":
    main()
