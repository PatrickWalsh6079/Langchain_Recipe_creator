
from langchain import PromptTemplate, LLMChain
from langchain.llms import GPT4All
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

def recipe_llm(items):
    template = """
    You are a helpful AI assistant that suggests recipes based on available ingredients.
    
    Create a recipe based on the following ingredients: {ingredients} and state how long it takes to create the meal. Give a catchy name to the recipe.
    """

    prompt = PromptTemplate(template=template, input_variables=["ingredients"])
    # Callbacks support token-wise streaming
    callbacks = [StreamingStdOutCallbackHandler()]

    # Verbose is required to pass to the callback manager
    llm = GPT4All(model="orca-mini-3b.ggmlv3.q4_0.bin", callbacks=callbacks, verbose=True)
    llm_chain = LLMChain(prompt=prompt, llm=llm)

    # ingredients = "Potatoes, hummus, onions, peppers, butter, salt and pepper"
    ingredients = items
    response = llm_chain.run(ingredients)

    return response
