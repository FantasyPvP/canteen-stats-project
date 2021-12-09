

PROJECT UPDATE LOG (please enter a log every time you update the google drive with a file)




08.12.21:

    - created grapher tool concept
    - created google drive for project
    - created README file
    - experimented with graph making functions in the matplotlib python package
        - use "pip install matplotlib" in command promt to install and "import matplotlib" to import
        - documentation for the module ----->  https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
        - used the module to create basic grapher where you can import the x and y values to plot in a bar chart




09.12.21:
    - bugfixed grapher tool
    - you can now provide an x and y input (X can be a label or integer, Y must be an integer)
    - created user profile generator in order to create test data for the algorithm
    - added a lot of comments to the code so that anyone can understand it and it is easier for other developers to find the right part of the code to make changes to
        (ive tried to name the variables as clearly as possible but if in doubt the comments will explain the purpose of each aspect of the code)
    - can create as many random student profiles as needed and plot the frequency of the meals bought on the graph automatically
        - the program can process over 12,000 values in about a second on my home computer (it should run even faster on a school computer given they have better multithreading than my computer)
        (i would guess 12000 is about the number of times someone used the canteen over a month although this could be very wrong)
        this assumes that the canteen is used around 600 times per day
            600 * 5 days = 3000 / week
            3000 * 4 weeks / month = 12000 / month
        - this shows that performance is unlikely to cause any problems and the algorithm should handle all of the data that the canteen can provide easily
