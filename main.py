import os

# 🐙 — many arms, one mind: parallel work, adaptive, tool-using.
def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write("🐙")

if __name__ == "__main__":
    main()
