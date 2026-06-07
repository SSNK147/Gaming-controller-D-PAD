import trimesh

original = trimesh.load(r"D:\SOFTAGE\1. D PAD\INPUTS\RetroPad - D-Pad.stl")
generated = trimesh.load(r"D:\SOFTAGE\1. D PAD\FINAL CODE\D PAD.stl")

print("Original Volume:", original.volume)
print("Generated Volume:", generated.volume)

difference = abs(original.volume - generated.volume)

print("Volume Difference:", difference)

if difference < 1e-6:
    print("PASS")
else:
    print("FAIL")