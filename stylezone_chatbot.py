"""
StyleZone PK — Clothing Shop Chatbot
Powered by Groq AI
Run: pip install groq
Then: python stylezone_chatbot.py
"""

from groq import Groq

# =============================================
#  SETUP: Paste your Groq API key here
#  Get free key at: https://console.groq.com
# =============================================
GROQ_API_KEY = "your_groq_api_key_here"

client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = """You are a helpful and friendly fashion assistant for StyleZone PK, an online clothing shop.
You ONLY talk about StyleZone PK. If someone asks anything unrelated, say:
"I can only help you with StyleZone PK related queries!"

SHOP INFO:
Name: StyleZone PK
Location: Lahore, Pakistan
WhatsApp: 0300-1234567

PRODUCTS & PRICES:
- Lawn Suit  = 2500 Rs
- Linen Shirt = 1800 Rs
- Jeans       = 3000 Rs
- Kurta       = 1500 Rs

DELIVERY: 3-5 working days (all over Pakistan)
HOW TO ORDER: WhatsApp at 0300-1234567

Be warm, friendly, and helpful. Keep answers clear and short. Only discuss shop-related topics.
"""

def chat():
    print("=" * 55)
    print("   👗  Welcome to StyleZone PK Chatbot  👗")
    print("=" * 55)
    print("Type your message. Type 'quit' to exit.\n")

    history = []

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() in ["quit", "exit", "bye"]:
            print("\nBot: Shukriya! Happy Shopping at StyleZone PK! 🛍️")
            break

        history.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    *history
                ],
                max_tokens=500,
                temperature=0.7,
            )

            reply = response.choices[0].message.content
            history.append({"role": "assistant", "content": reply})
            print(f"\nStyleZone PK: {reply}\n")

        except Exception as e:
            print(f"\n[Error]: {e}")
            print("Check your GROQ_API_KEY.\n")

if __name__ == "__main__":
    chat()
