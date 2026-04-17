"""Shared mock LLM used when no real API key is configured."""


def ask(question: str) -> str:
    q = question.lower().strip()

    if "docker" in q:
        return (
            "Docker is a container platform that packages an app and its "
            "dependencies so it runs consistently across environments."
        )
    if "deployment" in q or "deploy" in q:
        return (
            "Deployment is the process of releasing your application to an "
            "environment where users can access it."
        )
    if "cloud" in q:
        return (
            "Cloud deployment makes your application publicly reachable on "
            "managed infrastructure such as Railway, Render, or Cloud Run."
        )
    if "hello" in q or "hi" in q:
        return "Hello! Your production-ready agent is running."

    return (
        "This is a mock LLM response. The service is working correctly, "
        "and you can replace this with a real provider later."
    )
