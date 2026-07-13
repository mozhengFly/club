from nickname_generator import generate_nicknames

print("🎲 网名生成器测试")
print("=" * 30)

print("\n【随机风格】")
names = generate_nicknames(5, 'random')
for i, name in enumerate(names, 1):
    print(f"{i}. {name}")

print("\n【中文网名】")
names = generate_nicknames(5, 'chinese')
for i, name in enumerate(names, 1):
    print(f"{i}. {name}")

print("\n【英文网名】")
names = generate_nicknames(5, 'english')
for i, name in enumerate(names, 1):
    print(f"{i}. {name}")

print("\n【中英混合】")
names = generate_nicknames(5, 'mixed')
for i, name in enumerate(names, 1):
    print(f"{i}. {name}")

print("\n【特殊符号】")
names = generate_nicknames(5, 'special')
for i, name in enumerate(names, 1):
    print(f"{i}. {name}")