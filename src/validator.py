import logging

class PromptValidator:
    FORBIDDEN_PATTERNS = [
        "TheNitrome",
        "clarsimp",
        "SolidGoldMagikarp",
        ".bindingNavigatorMove",
        "etSocketAddress",
        ".scalablytyped",
        "JSGlobalScope"
    ]

    @staticmethod
    def peel_prompt(text: str) -> str:
        if not text:
            return text
            
        peel_text = text
        for pattern in PromptValidator.FORBIDDEN_PATTERNS:
            if pattern in text:
                logging.warning(f"Forbidden pattern detected: {pattern}")
            peel_text = peel_text.replace(pattern, "[FILTERED]")
            
        return peel_text
