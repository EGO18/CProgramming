class PathUtils:
    @staticmethod
    def get_extension(filename):
        """Return a file extension (including the dot)"""
        return filename[filename.rfind("."):] if "." in filename else ""
    
    #TODO
    @staticmethod
    #Return the directory path without the file name
    def get_directory(path):
        return
    #Return the file name from the directory path
    def get_basename(path):
        return os.path.basename(path)
    
#Use the class
print(PathUtils.get_extension("image.img"))
print(PathUtils.get_extension("1.txt"))
print(PathUtils.get_extension("test"))

print(PathUtils.get_directory("/Users/user/Desktop/report.pdf"))
print(PathUtils.get_basename("/Users/user/Desktop/report.pdf"))
print(PathUtils.get_directory("local_file.py"))
print(PathUtils.get_basename("local_file.py"))