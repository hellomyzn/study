import glob
import zipfile

with zipfile.ZipFile("test.zip", "w") as z:
    # z.write("testZip_dir")
    # z.write("testZip_dir/testZip.txt")

    for f in glob.glob("testZip_dir/**", recursive=True):
        print(f)
        z.write(f)


with zipfile.ZipFile("test.zip", "r") as z:
    z.extractall("zzz2")
