"""
Automated Environment Verification Utility
Role: Test environment baseline verification and runtime ping audit.
Author/Source: AI-assisted automation script for AI Red Teaming Lab setup.
Maintained by: Nooraldeen Dahshe
"""
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

samples = {
    "Short English": "Hello, world!",
    "Long English": "Artificial intelligence red teaming systematically probes machine learning pipelines for adversarial vulnerabilities.",
    "Code": "def login(user):\n    return user.is_admin",
    "Emoji String": "🚀🔥🤖🛡️⚡",
    "Arabic Sentence": "هذا اختبار لقياس كفاءة الترميز للغة العربية."
}

print(f"{'Type':<18} | {'Chars':<6} | {'Tokens':<6}")
print("-" * 35)
for label, text in samples.items():
    token_count = len(enc.encode(text))
    print(f"{label:<18} | {len(text):<6} | {token_count:<6}")
