#mutable

spice_mix = set()
print(f"Initial speice mix id: {id(spice_mix)}")
print(f"Initial speice mix id: {spice_mix}")

spice_mix.add("Ginger")
spice_mix.add("cardamom")

print(f"after speice mix id: {spice_mix}")

print(f"after speice mix id: {id(spice_mix)}")
 