import os
import subprocess


class Setup:
    def __init__(self):
        # List of dependencies to install
        # Open the file for reading
        with open("requirements.txt", "r") as file:
            # Read the file line by line
            lines = file.readlines()
        self.dependencies = []
        for line in lines:
            # Strip the whitespace from the line and add it to the list of names
            self.dependencies.append(line.strip())
        # Install each dependency that's not already installed
        for dependency in self.dependencies:
            if not self.dependency_installed(dependency):
                subprocess.run(["pip", "install", dependency])

    # Function to check if a dependency is installed
    def dependency_installed(self,dependency):
        # Try to import the dependency
        try:
            __import__(dependency)
        # If an ImportError is raised, the dependency is not installed
        except ImportError:
            return False
        # If no ImportError is raised, the dependency is installed
        else:
            return True

if __name__ == "__main__":
    # print(Setup.dependency_installed("tensorflow"))
    Setup()
Setup()
