# Crowdfunding Kit - Data Science Repo

## Application Goal - To predict the probability of a potential Kickstarter campaign to fail or succeed

### Backend API Link 
- https://ds-kickstarter-predict.herokuapp.com/predict

### Inputs required to make final prediction (as JSON)

- **Name**: Name of the kickstarter project
- **Blurb**: Description of the project
- **Campaign Length**: No. of days to raise the fund
- **USD Goal**: How much the project is trying to raise
- **Category**: Categories to choose from are:

        1. Art
        2. Crafts
        3. Comics
        4. Dance
        5. Design
        6. Fashion
        7. Film & Video
        8. Food
        9. Games
        10. Journalism
        11. Music
        12. Photography
        13. Publishing
        14. Technology
        15. Theater


## Predictive Model

Several different models were run to determine which produced the best predictions with the least complexity, including Random Forest Classifier, Multinomial Naive Bays, and a Keras Sequential Neural Network. Several natural language processing techniques were also tested, including tfidf vectorizer, SpaCy tokenization, and ELMo word embeddings. 

Baseline classification was 59.9%, and ultimately the highest level of accuracy reached within the weeklong scope of the project was 70.0%.

The model structure that reached this accuracy with the least complexity was:
- tfidf vectorizer to process text input (`Name` + `Blurb`)
- Multinomial Naive Bays model on concatenated text input
- predicted probability based on text input added as a new feature for final model
- Random Forest Classifier (`Text Classification Probability`, `USD Goal`, `Campaign Length`, `Category`)




