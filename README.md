# YouTube-GPT-Creator

![langchain_photo](https://github.com/YZLoh/autogpt_sample/assets/16683726/3e4eab0a-a375-4a01-b2c5-862f186c8ebc)

This project is a YouTube GPT Creator that generates YouTube video titles, scripts (potentially descriptions, tags, thumbnails) based on a given prompt. It utilizes the Langchain library, which is a powerful language model chaining framework.

## About 
Langchain is a framework that simplifies working with language models and enables creating complex conversational systems. It allows chaining together multiple language models, incorporating memories, and handling prompt templates effortlessly.

This project is mainly based off Nicolas Renotte's code. Visit his [YouTube channel](https://www.youtube.com/channel/UCjeijApQ06s7uH9vUT_d6Ww) and check out his insightful content on AI and NLP.
## Getting Started
To use the YouTube GPT Creator, follow the steps below:

### Installation
1. Clone the repository to your local machine.
2. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

### Usage
1. Run the application by executing the following command:
   ```
   streamlit run app.py 
   ```
2. Open the application in your web browser.
3. Enter your prompt in the provided text input field.
4. Click the "Generate" button to generate a YouTube video title and script based on your prompt.
5. View the generated title and script in the corresponding output sections.
6. Use the expanders to view the history of generated titles and scripts, as well as the Wikipedia research conducted.

## Dependencies
The YouTube GPT Creator requires the following dependencies:

- Python 3.7 or higher
- streamlit
- langchain
- WikipediaAPIWrapper

Feel free to explore different prompts and utilize the power of Langchain to generate engaging YouTube content effortlessly!
For a detailed explanation of the code and implementation, refer to the code documentation and the Langchain library documentation.

**Disclaimer**: This project is a demonstration of the capabilities of the Langchain framework and is not a fully functional production-ready application.

---

*This project is powered by the [Langchain](https://github.com/nicknochnack/Langchain-Crash-Course) crash course created by Nicolas Renotte.*
