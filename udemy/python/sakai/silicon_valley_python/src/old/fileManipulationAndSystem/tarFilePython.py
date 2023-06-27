import tarfile

with tarfile.open("test.tar.gz", "w:gz") as tr:
    tr.add("testTar_dir")

with tarfile.open("test.tar.gz", "r:gz") as tr:
    tr.extractall(path="test_tar")
