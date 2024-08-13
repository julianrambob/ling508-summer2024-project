# ling508-summer2024-project

### Description
This application serves as a study tool for Russian morphological forms, focusing on first declension nouns. Users can submit a noun in the nominative singular form to the database, and the app generates its corresponding forms for each case and number. The application allows users to add multiple nouns for study and offers a refresh option to clear the database.

### Installation
To run the project using docker:

1. **Open you local repository folder in a terminal and run the following commands**
    
   ```bash
   git clone https://github.com/julianrambob/ling508-summer2024-project 
   ```
   
   ```bash
   cd ling508-summer2024-project
   ```
   
   ```bash
   docker-compose up --build
   ```

   
2. **Click on the link generated in the terminal**
   ```bash
    * Running on http://127.0.0.1:5000
   ```
   **or open a browser and enter url: http://localhost:5000/**
### Project Next Steps
The repository includes preliminary structures to support flashcard functions for Russian verbs. Future development could involve integrating data from an established Russian lexicon. Russian morphology is complex, with many irregular forms and endings. Incorporating existing lexicon data would improve the accuracy of generated noun forms.

### Notes
The current application is not yet reliable for comprehensive study of Russian nouns. Even within first declension nouns, there are unpredictable endings—particularly in the accusative plural, where some nouns align with the nominative plural and others with the genitive plural. This app currently defaults to nominative forms in these cases.
More input validation is also needed to decrease possible errors. 

Further documentation in the documents directory