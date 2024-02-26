from script.app import App

def setup_readme():
    with open('Readme.txt', 'w') as file:
        file.write("Owner : Sudip \nEmail: sudip.halder.21@aot.edu.in")

if __name__ == "__main__":
    setup_readme()
    __app = App()
    __app.run()