'''This code generates a visualization of the most distinctive words for four genres: detective, horror, adventure and historical.

Here's how the code works:

    The necessary packages are imported: scattertext, pandas, and glob.
    A corpus list is initialized to hold the texts and genre labels of the files that will be read in.
    The script iterates through the folders containing the text files for each genre, reading in each file and adding its text and genre label to the corpus list.
    The corpus list is converted into a pandas DataFrame.
    The text data in the DataFrame is preprocessed using the whitespace_nlp_with_sentences method from scattertext.
    A scattertext Corpus object is created from the parsed texts in the DataFrame and the genre labels.
    The top 10 distinctive words for each genre are extracted using tf-idf scoring.
    The distinctive words for each genre are printed to the console.
    A scattertext visualization is created using the produce_scattertext_explorer method. This method takes in several parameters, including the corpus, the category to focus on (in this case, 'detective'), the names for the category and non-category (i.e., 'Other Genres'), the minimum frequency for a term to be included, and the width of the visualization in pixels.
    The resulting visualization is saved to an HTML file named 'scattertext_visualization.html'.

Overall, this code demonstrates how to use scattertext to create a visualization that highlights the most distinctive words in a corpus for different genres.'''

import scattertext as st 
import pandas as pd 
import glob

# Load the corpus 
corpus = [] 

# Add the text files to the corpus 
for genre in ['detective', 'horror', 'adventure', 'historical']:
    for file_path in glob.glob(f"{genre}/*.txt"):
        with open(file_path, 'r', encoding='utf-8') as f:
            corpus.append({'text': f.read(), 'genre': genre}) 

# Convert the corpus into a DataFrame 
df = pd.DataFrame(corpus)

# Preprocess the text 
nlp = st.whitespace_nlp_with_sentences 
df['parsed'] = df['text'].apply(nlp) 

# Create the corpus using the parsed texts and the genre labels 
corpus = st.CorpusFromParsedDocuments(df, category_col='genre', parsed_col='parsed').build() 

# Use tf-idf to extract the top 10 distinctive words per genre 
term_freq_df = corpus.get_term_freq_df()
term_freq_df['detective'] = corpus.get_scaled_f_scores('detective')
term_freq_df['horror'] = corpus.get_scaled_f_scores('horror')
term_freq_df['adventure'] = corpus.get_scaled_f_scores('adventure')
term_freq_df['historical'] = corpus.get_scaled_f_scores('historical')
term_freq_df['max_genre'] = term_freq_df[['detective', 'horror', 'adventure', 'historical']].idxmax(axis=1)
for genre in ['detective', 'horror', 'adventure', 'historical']:
    print(f"\nTop 10 distinctive words for {genre}:")
    print(term_freq_df.sort_values(by=genre, ascending=False).index[:10])

# Use scattertext to create the visualization 
html = st.produce_scattertext_explorer(
    corpus,
    category='detective',
    category_name='Detective',
    not_category_name='Other Genres',
    use_full_doc=True,      
    minimum_term_frequency=5, 
    width_in_pixels=1000, 
    metadata=df['genre'], 
    metadata_descriptions=None, 
    sort_by_dist=False, 
    #color_by_term_frequency=True
) 

# Save the result to an HTML file
open('scattertext_visualization.html', 'wb').write(html.encode('utf-8'))


