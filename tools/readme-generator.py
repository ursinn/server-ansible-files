import glob
import os

path = r'C:\Users\xxx\server-ansible-files\roles\*'  # give the path where all the folders are located

for directory_path in glob.glob(path):
    if os.path.isdir(directory_path):
        os.chdir(directory_path)
        folder_name = os.path.basename(directory_path)
        if os.path.exists("README.md") == False:
            print(folder_name)
            readme_file = open("README.md", "w")
            readme_file.write("# " + folder_name + "\n")
            readme_file.write("\n")
            readme_file.write("[![GitHub last commit](https://img.shields.io/github/last-commit/ursinn/" + folder_name + "?logo=github&style=for-the-badge)](https://github.com/ursinn/" + folder_name + "/commits)\n")
            readme_file.write("[![License](https://img.shields.io/github/license/ursinn/" + folder_name + "?style=for-the-badge)](https://github.com/ursinn/" + folder_name + "/blob/main/LICENSE)\n")
            readme_file.write("\n")
            readme_file.write("## License\n")
            readme_file.write("\n")
            readme_file.write("This project is under the MIT License. See the [LICENSE](https://github.com/ursinn/" + folder_name + "/blob/main/LICENSE) file for the full license text.\n")
            readme_file.close() 
        
