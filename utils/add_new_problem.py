import datetime
import os


def get_filename_title(title):
    title = title.replace(" ", "_")
    title = title.replace(".", "_")
    title = title.replace("__", "_")
    return title


def update_readme(title, filename_title, url, category):
    with open("../README.md", "a") as readme:
        readme.write(
            "| [{}]({}) | {} | [Solution](solutions/{}) |\n".format(title, url,
                                                                    category,
                                                                    filename_title))


def make_problem_directory(repo_path, filename_title):
    directory = os.path.join(repo_path, "solutions", filename_title)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return str(directory)


def make_solution_file(title, category, url, username, directory_path,
                       extension='.py'):
    filename = "solution_" + username + extension
    file_path = os.path.join(directory_path, filename)
    with open(file_path, "w") as f:
        f.writelines(write_file_header(title, category, url, username))
    return file_path


def write_file_header(title, category, url, username):
    created_date = datetime.datetime.today().strftime("%d %B %Y")
    header_str = '\'\'\'\n'
    header_str += 'Title     : ' + title + '\n'
    header_str += 'Category  : ' + category + '\n'
    header_str += 'URL       : ' + url + '\n'
    header_str += 'Author    : ' + username + '\n'
    header_str += 'Created   : ' + created_date + '\n'
    header_str += '\'\'\'\n'
    return header_str


title = input("Add new problem title: ").strip()
filename_title = get_filename_title(title)
url = input("Add new problem url: ").strip()
category = input("Problem Type: ").strip()
username = input("Username (keep blank for arsho): ").strip()
extension = input("Extension (keep blank for .py): ").strip()
if username == '':
    username = 'arsho'
if extension == '':
    extension = '.py'
current_path = os.path.dirname(os.path.realpath(__file__))
repo_path = os.path.abspath(os.path.join(current_path, os.pardir))
update_readme(title, filename_title, url, category)
directory = make_problem_directory(repo_path, filename_title)
filepath = make_solution_file(title, category, url, username, directory,
                              extension)
print("Done. Open {}".format(filepath))
