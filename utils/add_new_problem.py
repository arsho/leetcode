import os

def get_filename_title(title):
    title = title.replace(" ","_")
    title = title.replace(".","_")
    return title

def update_readme(title, filename_title, url, category):
    with open("../README.md", "a") as readme:
        readme.write("| [{}]({}) | {} | [Solution](solutions/{}) |\n".format(title, url, category, filename_title))


def make_problem_directory(repo_path, filename_title):
    directory = os.path.join(repo_path,"solutions",filename_title)
    if not os.path.exists(directory):
        os.makedirs(directory)

title = "121. Best Time to Buy and Sell Stock"#input("Add new problem title: ")
filename_title = get_filename_title(title)
url = "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/"#input("Add new problem url: ")
category = "Dynamic Programming"#input("Problem Type: ")
current_path = os.path.dirname(os.path.realpath(__file__))
repo_path = os.path.abspath(os.path.join(current_path, os.pardir))
update_readme(title, filename_title, url, category)
make_problem_directory(repo_path, filename_title)
