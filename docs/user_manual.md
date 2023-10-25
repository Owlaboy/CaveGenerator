## User manual

### Setting up the program

The program uses poetry for package/version management. If you do not have poetry installed, install it first.

After installing poetry you can install the required packages by running the following command in the root directory of the program.

``poetry install``

### Running the program

To start the program we can use invoke tasks. Run the following command in the root directory of the project.

```poetry run invoke start```

Once the program has started it asks a few questions from you in the command line. After aswering the questions the program is run with the given inputs. Once the final map is displayed the program can be restarted by pressing any key, returing the user to the command line to answer the questions again.

### Testing and coverage

You can run the automated tests by executing the following command. Generating a coverage report is also below.

```poetry run invoke test```

``poetry run invoke coverage-report``