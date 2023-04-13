# Finding distinctive words per genre

## Data 
The exploration corpus consists of novels in four different genres: detective, historical, adventure and horror. All novels are written by Arthur Conan Doyle.

## Packages 
The necessary packages are: scattertext, pandas, and glob.

## Method

    A corpus list is initialized to hold the texts and genre labels of the files that will be read in.
    The script iterates through the folders containing the text files for each genre, reading in each file and adding its text and genre label to the corpus list.
    The corpus list is converted into a pandas DataFrame.
    The text data in the DataFrame is preprocessed using the whitespace_nlp_with_sentences method from scattertext.
    A scattertext corpus object is created from the parsed texts in the DataFrame and the genre labels.
    The top 15 distinctive words for each genre are extracted using tf-idf scoring.
    The distinctive words for each genre are printed to the console.
    A scattertext visualization is created using the produce_scattertext_explorer method. This method takes in several parameters, including the corpus, the category to focus on (in this case, 'detective'), the names for the category and non-category (i.e., 'Other Genres'), the minimum frequency for a term to be included, and the width of the visualization in pixels.
    The resulting visualization is saved to an HTML file named 'scattertext_visualization.html'.
    
    
 ## Results
 Top 15 distinctive ngrams for detective:
Index(['holmes', 'watson', 'sherlock', 'sherlock holmes', 'baskerville',
       'sir henry', 'the moor', 'sir charles', 'stapleton', 'moor', 'mortimer',
       'said holmes', 'henry', 'dr', 'sholto'],
      dtype='object', name='term')

Top 15 distinctive ngrams for horror:
Index(['haw', 'raffles', 'raffles haw', 'mcintyre', 'robert', 'laura',
       'penclosa', 'wilson', 'agatha', 'miss penclosa', 'hector', 'his father',
       'laboratory', 'said robert', 'money'],
      dtype='object', name='term')

Top 15 distinctive ngrams for adventure:
Index(['lord john', 'summerlee', 'challenger', 'professor challenger',
       'plateau', 'professor', 'said lord', 'roxton', 'said challenger',
       'professor summerlee', 'the plateau', 'the professor', 'malone', 'ape',
       'creatures'],
      dtype='object', name='term')

Top 15 distinctive ngrams for historical:
Index(['alleyne', 'nigel', 'sir nigel', 'catinat', 'de catinat', 'sire',
       'amos', 'aylward', 'hath', 'nay', 'de', 'the king', 'king', 'madame',
       'france'],
      dtype='object', name='term')
      
 ## Visualization of distinctive words in detective fiction (Doyle corpus) 


![Distinctive words in detective fiction](https://raw.githubusercontent.com/roettger/Doyle/main/scattertext.PNG)


## Read on

Lavin, Matthew J. (2019): "Analyzing Documents with TF-IDF", in: Programming Historian: https://doi.org/10.46430/phen0082.

